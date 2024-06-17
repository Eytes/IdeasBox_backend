from abc import ABC, abstractmethod

from ..base_types import ItemId, T


class AbstractRepository(ABC):
    def __init__(self, repository):
        self._repository = repository

    @abstractmethod
    async def get(self, item_id: ItemId) -> T | None:
        pass

    @abstractmethod
    async def create(self, new_item: T) -> T:
        pass

    @abstractmethod
    async def update(self, item_id: ItemId, new_item_data: T) -> T | None:
        pass

    @abstractmethod
    async def delete(self, item_id: ItemId) -> T | None:
        pass
