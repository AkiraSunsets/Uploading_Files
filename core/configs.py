from typing import ClassVar
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = 'postgresql+asyncpg://postgres:root@127.0.0.1:5432/faculdade'
    DBBaseModel: ClassVar = declarative_base()

    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env"
    )

settings = Settings()