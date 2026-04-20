from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    environment: str = "local"
    log_level: str = "INFO"
    default_provider: str = "mock"

    class Config:
        env_file = ".env"

settings = Settings()
