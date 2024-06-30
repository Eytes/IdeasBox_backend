from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from ..config import settings


class MongoDBHelper:
    def __init__(self, database_url: str) -> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(
            database_url,
            UuidRepresentation="standard",  # чтобы uuid генерировалось синхронизировано с python
        )
        self.db: AsyncIOMotorDatabase = self.client.get_database()

    def repository_factory[
        MongoRepository
    ](self, repository: type[MongoRepository]) -> MongoRepository:
        """
        Фабрика создания репозитория для CRUD операций над коллекцией.
        Имя коллекции генерируется автоматически на основе названия класса репозитория.
        """
        collection_name = (
            repository.__name__.lower().replace("mongo", "").replace("repository", "")
        )
        return repository(self.db[collection_name])


mongo_helper = MongoDBHelper(database_url=settings.mongodb.url)
