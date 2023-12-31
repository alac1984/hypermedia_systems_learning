from pydantic import BaseSettings


class AppSettings(BaseSettings):
    DATABASE_URL: str
    DEBUG_MODE: bool = False

    class Config:
        env_file = ".env"
