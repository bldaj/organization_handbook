from pathlib import (
    Path,
)

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"


class Settings(BaseSettings):
    # Project
    API_V1_STR: str = '/api/v1'

    model_config = SettingsConfigDict(env_file=ENV_PATH)
