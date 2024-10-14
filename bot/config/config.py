from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    REF_ID: str = '00006uXQ'
    
    FAKE_USERAGENT: bool = True
    
    AUTO_PLAY_GAME: bool = True
    POINTS_COUNT: list[int] = [450, 600]
    
    AUTO_SPIN: bool = True
    AUTO_TASK: bool = True
    AUTO_DAILY_REWARD: bool = True
    AUTO_CLAIM_STARS: bool = True
    AUTO_CLAIM_COMBO: bool = True
    AUTO_RANK_UPGRADE: bool = True
    
    AUTO_FARM: bool = True
    USE_RANDOM_DELAY_IN_FARM: bool = True
    RANDOM_DELAY_IN_FARM: list[int] = [1200, 1800]

    USE_RANDOM_DELAY_IN_RUN: bool = True
    RANDOM_DELAY_IN_RUN: list[int] = [0, 15]

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()