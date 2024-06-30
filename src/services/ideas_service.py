from ..core.base_types import ItemId
from ..core.db.abstract_repository import Repository
from ..schemas.idea import IdeaSchema, IdeaBaseSchema, IdeaUpdateSchema


class IdeasService:
    def __init__(self, repository: Repository) -> None:
        self.repository = repository

    async def get_own_ideas(self) -> list[IdeaSchema]:
        pass

    async def create_idea(self, new_idea: IdeaBaseSchema) -> IdeaSchema:
        pass

    async def update_own_idea(
        self,
        idea_id: ItemId,
        new_idea_data: IdeaUpdateSchema,
    ) -> IdeaSchema:
        pass

    def delete_own_idea(self, idea_id: ItemId) -> IdeaBaseSchema:
        pass
