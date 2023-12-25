from pydantic import BaseSettings


class AppSettings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:a1k8u2@localhost:dummy/dummy"
    DEBUG_MODE: bool = False

    class Config:
        env_file = ".env"
