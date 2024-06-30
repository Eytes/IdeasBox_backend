from pydantic import BaseModel, Field

from core.config import settings
from core.utils import formatted_time_now
from .mixins import IdMixin


class IdeaBaseSchema(BaseModel):
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


class IdeaSchema(IdMixin, IdeaBaseSchema):
    pass
