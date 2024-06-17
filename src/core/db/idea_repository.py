from schemas.idea import IdeaSchema
from .abstract_reposytory import AbstractRepository
from ..base_types import ItemId


class IdeasRepository(AbstractRepository):
    async def get(self, item_id: ItemId) -> IdeaSchema | None:
        pass

    async def create(self, new_item: IdeaSchema) -> IdeaSchema:
        pass

    async def update(
            self,
            item_id: ItemId,
            new_item_data: IdeaSchema,
    ) -> IdeaSchema | None:
        pass

    async def delete(self, item_id: ItemId) -> IdeaSchema | None:
        pass
