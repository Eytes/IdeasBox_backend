from uuid import uuid4

from pydantic import BaseModel, Field

from core.base_types import ItemId


class IdMixin(BaseModel):
    id: ItemId = Field(
        default_factory=lambda: ItemId(uuid4()),
        alias="_id",
    )
