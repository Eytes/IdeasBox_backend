from typing import Type


class MongoRepositoryFactory[DatabaseType]:
    def __init__(self, database: DatabaseType):
        self.__database = database

    def create_collection_and_get_repository[
        MongoRepository
    ](self, repository: Type[MongoRepository]) -> MongoRepository:
        """Автоматически создается коллекция и набор CRUD операций для этой коллекции"""
        collection_name = (
            repository.__name__.lower().replace("mongo", "").replace("repository", "")
        )
        return repository(self.__database[collection_name])
