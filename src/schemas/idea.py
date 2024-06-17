from pydantic import Field

from core.config import settings
from .mixins import IdMixin


class IdeaSchema(IdMixin):
    title: str = Field(
        min_length=settings.idea.min_title_length,
        max_length=settings.idea.max_title_length,
    )
    description: str = Field(
        min_length=settings.idea.min_title_length,
        max_length=settings.idea.max_description_length,
    )
