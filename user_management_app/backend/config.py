from pydantic import SecretStr
from pydantic_settings import BaseSettings , SettingsConfigDict 
 
# SettingsConfigDict -> automatically load values from .env files

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


    secret_key: SecretStr
    database_url : str

    algorithm: str = "HS256" 
    access_token_expire_minutes : int = 10
    refresh_token_expire_days: int = 7


settings = Settings() 
