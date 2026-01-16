from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables or a .env file.

    The SettingsConfigDict ensures that environment variables take precedence,
    followed by values defined in the '.env' file.
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Logging
    DEV_MODE: bool = False

    # Example for external scraping, e.g., an API Key
    # EXTERNAL_API_KEY: str = ""
