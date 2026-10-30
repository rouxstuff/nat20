from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = "sqlite:///./nat20.db"
    # TODO: secret_key (str), dev pattern
    model_config = SettingsConfigDict(env_file=".env") 

settings = Settings()
