import os

from pydantic import SecretStr, model_validator, BaseModel, PositiveInt
from pydantic_settings import BaseSettings
from typing_extensions import Self


class MongoSettings(BaseModel):
    root_username: str = os.getenv("MONGO_ROOT_USERNAME")  # type: ignore[assignment]
    password: SecretStr = os.getenv("MONGO_ROOT_PASSWORD")  # type: ignore[assignment]
    host: str = os.getenv("MONGO_HOST")  # type: ignore[assignment]
    port: int = os.getenv("MONGO_PORT")  # type: ignore[assignment]
    database_name: str = os.getenv("MONGO_DATABASE_NAME")  # type: ignore[assignment]
    url: str | None = None

    @model_validator(mode="after")
    def create_url(self) -> Self:
        self.url = f"mongodb://{self.root_username}:{self.password.get_secret_value()}@{self.host}:{self.port}"
        return self


class IdeaSettings(BaseModel):
    max_title_length: PositiveInt = 64
    min_title_length: PositiveInt = 1
    max_description_length: PositiveInt = 512
    min_description_length: PositiveInt = 1


class Settings(BaseSettings):
    mongodb: MongoSettings = MongoSettings()
    idea: IdeaSettings = IdeaSettings()
    api_v1_prefix: str = "/api/v1"
    time_format: str = "%d/%m/%Y, %H:%M:%S"


settings = Settings()
