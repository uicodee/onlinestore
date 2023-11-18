from pydantic_settings import BaseSettings


class DB(BaseSettings):

    host: str  # localhost
    port: int  # 5432
    name: str  # onlinestore
    user: str  # postgres
    password: str  # postgres


# class Api(BaseSettings):
#
#     secret: str


class SettingsExtractor(BaseSettings):
    DB__HOST: str
    DB__PORT: int
    DB__NAME: str
    DB__USER: str
    DB__PASSWORD: str

    # API__SECRET: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class Settings(BaseSettings):
    db: DB


def load_settings() -> Settings:
    settings = SettingsExtractor()

    return Settings(
        db=DB(
            host=settings.DB__HOST,
            port=settings.DB__PORT,
            name=settings.DB__NAME,
            user=settings.DB__USER,
            password=settings.DB__PASSWORD,
        )
    )
