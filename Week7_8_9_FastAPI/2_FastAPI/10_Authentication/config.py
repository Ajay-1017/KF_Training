from pydantic import SecretStr
from pydantic_settings import BaseSettings , SettingsConfigDict 
 
# SettingsConfigDict -> automatically load values from .env files

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


    secret_key: SecretStr # it wont leak the value at logs or in prints
    algorithm: str = "HS256" # it is standard for json web tokens
    access_token_expire_minutes : int = 30


settings = Settings() # Loaded from .env file


# Mental model flow chart


        #                            config.py
        #                                │
        #                                │
        #                                ▼
        #             ┌──────────────────────────────────┐
        #             │ class Settings(BaseSettings):    │
        #             └──────────────────────────────────┘
        #                                │
        #                                │
        #                                ▼
        #        "BaseSettings = Configuration Loader"
        #        (Its job is to build one Settings object
        #          by collecting configuration values.)
        #                                │
        #                                │
        #                                ▼
        #  ┌─────────────────────────────────────────────────────────────┐
        #  │ model_config = SettingsConfigDict(                          │
        #  │                                                             │
        #  │     env_file=".env",                                        │
        #  │     env_file_encoding="utf-8"                               │
        #  │ )                                                           │
        #  └─────────────────────────────────────────────────────────────┘
        #                                │
        #                                │
        #                                ▼
        #   "SettingsConfigDict tells BaseSettings HOW to load settings."
        #                                │
        #                                │
        #                                ▼
        #         ┌──────────────────────────────────────┐
        #         │ Look for a file named ".env"         │
        #         │ Read it using UTF-8 encoding         │
        #         └──────────────────────────────────────┘
        #                                │
        #                                ▼
        #                    Opens the .env file
        #                                │
        #                                ▼

        #    SECRET_KEY=9573fc9c8200a58ab80143d41126ae...
        #    ACCESS_TOKEN_EXPIRE_MINUTES=30
        #    ALGORITHM=HS256

        #                                │
        #                                ▼
        #      BaseSettings now knows all available values
        #                                │
        #                                ▼
        #      Reads every field declared in Settings class

        #            secret_key : SecretStr
        #            algorithm : str = "HS256"
        #            access_token_expire_minutes : int = 30

        #                                │
        #                                ▼
        #  For each field, BaseSettings searches in this order

        #       Environment Variable (Highest Priority)
        #                    │
        #             Found?
        #           Yes │        No
        #               ▼         │
        #      Use this value     ▼
        #                    Check .env file
        #                           │
        #                    Found?
        #                 Yes │        No
        #                     ▼         │
        #             Use .env value    ▼
        #                        Use default value
        #                               │
        #                        (if available)
        #                               │
        #                               ▼
        #                  If nothing exists anywhere
        #                               │
        #                               ▼
        #                   Raise Validation Error
        #                  ("Required setting missing")

        #                               │
        #                               ▼
        #          Convert values into proper Python types

        #   SECRET_KEY  ─────► SecretStr
        #   "30"        ─────► int(30)
        #   "HS256"     ─────► str

        #                               │
        #                               ▼
        #          Create one Settings object in memory

        #                settings = Settings()

        #                               │
        #                               ▼
        #      settings
        #      ├── secret_key
        #      ├── algorithm
        #      └── access_token_expire_minutes

        #                               │
        #                               ▼
        #   Anywhere in the FastAPI project

        #   from config import settings

        #   settings.secret_key
        #   settings.algorithm
        #   settings.access_token_expire_minutes