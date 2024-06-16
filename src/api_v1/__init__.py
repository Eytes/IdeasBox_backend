from fastapi import APIRouter

from ..core.config import settings

api_v1 = APIRouter(
    prefix=settings.api_v1_prefix,
    tags=["APIv1"],
)
