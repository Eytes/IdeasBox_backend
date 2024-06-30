from abc import ABC, abstractmethod


class Repository[IdType, BaseSchema, UpdateSchema, Schema](ABC):

    @abstractmethod
    async def get(self, item_id: IdType) -> Schema | None: ...

    @abstractmethod
    async def create(self, new_item: BaseSchema) -> IdType: ...

    @abstractmethod
    async def update(
        self,
        item_id: IdType,
        new_item_data: UpdateSchema,
    ) -> Schema | None: ...

    @abstractmethod
    async def delete(self, item_id: IdType) -> BaseSchema | None: ...


class MongoRepository[CollectionType, IdType, BaseSchema, UpdateSchema, Schema](
    Repository[IdType, BaseSchema, UpdateSchema, Schema],
    ABC,
):
    def __init__(self, collection: CollectionType) -> None:
        self._collection = collection
