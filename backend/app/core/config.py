from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Managers Daily Report"
    environment: str = "local"
    demo_mode: bool = True

    database_url: str = (
        "postgresql+psycopg://postgres:postgres@localhost:5432/"
        "managers_daily_report"
    )
    storage_backend: str = "postgres"

    timezone: str = "Europe/Moscow"
    morning_reminder_time: str = "09:00"
    afternoon_reminder_time: str = "13:00"
    evening_reminder_time: str = "17:00"

    cors_origins: list[str] = ["http://localhost:5173"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
