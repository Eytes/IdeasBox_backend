from typing import Annotated

from pydantic import UUID4

ItemId = Annotated[str, UUID4]
