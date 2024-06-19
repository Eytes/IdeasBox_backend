from motor.motor_asyncio import AsyncIOMotorClient

from .ideas_repository import IdeasMongoRepository
from .mongo import MongoRepositoryFactory
from ..config import settings

__client = AsyncIOMotorClient(settings.mongodb.url)
__db = __client[settings.mongodb.database_name]

repository_factory = MongoRepositoryFactory(__db)
ideas_repository = repository_factory.create_collection_and_get_repository(
    IdeasMongoRepository
)
