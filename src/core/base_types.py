from typing import Annotated, TypeVar

from pydantic import UUID4

ItemId = Annotated[str, UUID4]
T = TypeVar("T")
