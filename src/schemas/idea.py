from typing import Self

from pydantic import BaseModel, Field, model_validator

from .mixins import IdMixin
from ..core.base_types import ItemId
from ..core.config import settings
from ..core.utils import formatted_time_now


class IdeaBaseSchema(BaseModel):
    user_id: ItemId
    title: str = Field(
        min_length=settings.idea.min_title_length,
        max_length=settings.idea.max_title_length,
    )
    description: str = Field(
        min_length=settings.idea.min_title_length,
        max_length=settings.idea.max_description_length,
    )
    create_at: str = formatted_time_now()
    update_at: str = create_at


class IdeaUpdateSchema(BaseModel):
    title: str | None = Field(
        min_length=settings.idea.min_title_length,
        max_length=settings.idea.max_title_length,
    )
    description: str | None = Field(
        min_length=settings.idea.min_title_length,
        max_length=settings.idea.max_description_length,
    )
    update_at: str = formatted_time_now()

    @model_validator(mode="after")
    def all_is_not_none(self) -> Self:
        if not (self.title or self.description):
            raise ValueError("At least one field must be filled in")
        return self


class IdeaSchema(IdMixin, IdeaBaseSchema):
    pass
