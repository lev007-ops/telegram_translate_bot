from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    oauth_token: str
    folder_id: str
    version: str


@dataclass
class Postgres:
    database: str
    user: str
    password: str
    host: str


@dataclass
class Config:
    tg_bot: TgBot
    misc: Miscellaneous
    db: Postgres


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS")
        ),
        misc=Miscellaneous(
            oauth_token=env.str("OAUTH_TOKEN"),
            folder_id=env.str("FOLDER_ID"),
            version="1.1.1"
        ),
        db=Postgres(
            database=env.str("DB_NAME"),
            user=env.str("DB_USER"),
            password=env.str("DB_PASSWORD"),
            host=env.str("DB_HOST")
        )
    )
