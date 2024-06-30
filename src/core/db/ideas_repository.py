from typing import override

from motor.motor_asyncio import AsyncIOMotorCollection

from schemas.idea import IdeaSchema, IdeaBaseSchema, IdeaUpdateSchema
from .abstract_repository import MongoRepository
from ..base_types import ItemId


class IdeasMongoRepository(
    MongoRepository[
        AsyncIOMotorCollection,
        ItemId,
        IdeaBaseSchema,
        IdeaUpdateSchema,
        IdeaSchema,
    ]
):
    @override
    async def get(self, item_id: ItemId) -> IdeaSchema | None:
        """Получить запись из БД по id"""
        raw_data: dict | None = await self._collection.find_one({"_id": item_id})
        return IdeaSchema(**raw_data) if raw_data else None

    @override
    async def create(self, new_item: IdeaBaseSchema) -> ItemId:
        """Создание записи в БД"""
        idea = IdeaSchema(**new_item.model_dump())
        return (
            await self._collection.insert_one(idea.model_dump(by_alias=True))
        ).inserted_id

    @override
    async def update(
        self,
        item_id: ItemId,
        new_item_data: IdeaUpdateSchema,
    ) -> IdeaSchema | None:
        """Обновление данных в БД. Обновляются только измененные поля (поля != None)."""
        raw_new_data: dict | None = await self._collection.find_one_and_update(
            {"_id": item_id},
            {"$set": new_item_data.model_dump(exclude_none=True)},
        )
        return IdeaSchema(**raw_new_data) if raw_new_data else None

    @override
    async def delete(self, item_id: ItemId) -> IdeaBaseSchema | None:
        """Удаление записи из БД"""
        old_raw_data: dict | None = await self._collection.find_one_and_delete(
            {"_id": item_id}
        )
        return IdeaBaseSchema(**old_raw_data) if old_raw_data else None
