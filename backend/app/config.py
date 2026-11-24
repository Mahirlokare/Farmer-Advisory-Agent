from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Bharat Krishi AI API"
    environment: str = "development"
    cors_origins: str = "http://localhost:5173"
    open_meteo_base_url: str = "https://api.open-meteo.com/v1/forecast"
    llm_api_key: str | None = None
    llm_base_url: str = "https://api.openai.com/v1"
    llm_model: str = "gpt-4o-mini"
    llm_timeout_seconds: float = 45.0
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
