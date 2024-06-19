from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseModel


class Repository[IdType, Schema: Type[BaseModel]](ABC):

    _base_schema: Schema

    @abstractmethod
    async def get(self, item_id: IdType) -> Schema | None: ...

    @abstractmethod
    async def create(self, new_item: Schema) -> IdType: ...

    @abstractmethod
    async def update(self, item_id: IdType, new_item_data: Schema) -> Schema | None: ...

    @abstractmethod
    async def delete(self, item_id: IdType) -> Schema | None: ...

    @classmethod
    def _convert_to_schema(cls, data_dict: dict | None) -> Schema | None:
        if not issubclass(cls._base_schema, BaseModel):
            raise TypeError("cls._base_schema is not a subclass of the BaseModel")
        return cls._base_schema(**data_dict) if data_dict else None


class MongoRepository[IdType, CollectionType, Schema](Repository[IdType, Schema], ABC):
    def __init__(self, collection: CollectionType) -> None:
        self._collection = collection
