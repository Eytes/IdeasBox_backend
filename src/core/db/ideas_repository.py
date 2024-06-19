from typing import override

from motor.motor_asyncio import AsyncIOMotorCollection

from schemas.idea import IdeaBaseSchema
from .abstract_repository import MongoRepository
from ..base_types import ItemId


class IdeasMongoRepository(
    MongoRepository[
        ItemId,
        AsyncIOMotorCollection,
        IdeaBaseSchema,
    ]
):
    _base_schema = IdeaBaseSchema

    @override
    async def get(self, item_id: ItemId) -> IdeaBaseSchema | None:
        """Получить запись из БД по id"""
        raw_data = await self._collection.find_one({"_id": item_id})
        return self._convert_to_schema(raw_data)

    @override
    async def create(self, new_item: IdeaBaseSchema) -> ItemId:
        """Создание записи в БД"""
        result = await self._collection.insert_one(new_item.model_dump(by_alias=True))
        return result.inserted_id

    @override
    async def update(
        self,
        item_id: ItemId,
        new_item_data: IdeaBaseSchema,
    ) -> IdeaBaseSchema | None:
        """Обновление данных в БД"""
        raw_new_data = await self._collection.find_one_and_update(
            {"_id": item_id},
            {"$set": new_item_data.model_dump()},
        )
        return self._convert_to_schema(raw_new_data)

    @override
    async def delete(self, item_id: ItemId) -> IdeaBaseSchema | None:
        """Удаление записи из БД"""
        old_raw_data = await self._collection.find_one_and_delete({"_id": item_id})
        return self._convert_to_schema(old_raw_data)
