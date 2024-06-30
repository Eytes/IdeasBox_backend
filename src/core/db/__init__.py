from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from .ideas_repository import IdeasMongoRepository
from .mongo_repository_factory import MongoRepositoryFactory
from ..config import settings

__client: AsyncIOMotorClient = AsyncIOMotorClient(
    settings.mongodb.url,
    UuidRepresentation="standard",  # чтобы uuid генерировалось синхронизировано с python
)
__db = __client[settings.mongodb.database_name]

repository_factory = MongoRepositoryFactory[AsyncIOMotorDatabase](__db)
ideas_repository = repository_factory.create_collection_and_get_repository(
    IdeasMongoRepository
)
