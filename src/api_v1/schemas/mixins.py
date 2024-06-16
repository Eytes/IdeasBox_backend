from uuid import uuid4

from pydantic import BaseModel, Field

from ..base_types import ItemId


class IdMixin(BaseModel):
    id: ItemId = Field(default_factory=lambda: ItemId(uuid4()))
