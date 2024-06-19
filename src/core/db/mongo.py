from typing import Type

from motor.motor_asyncio import AsyncIOMotorDatabase


class MongoRepositoryFactory:
    def __init__(self, database: AsyncIOMotorDatabase):
        self.__database = database

    def create_collection_and_get_repository[
        MongoRepository
    ](self, repository: Type[MongoRepository]) -> MongoRepository:
        """Автоматически создается коллекция и набор CRUD операций для этой коллекции"""
        collection_name = repository.__name__.lower().replace("repository", "")
        return repository(self.__database[collection_name])
