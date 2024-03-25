from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    DATABASE_URL: str
    DATABASE_URL_OUT: str
    DEBUG_MODE: bool = False
    model_config = SettingsConfigDict(env_file=".env")
