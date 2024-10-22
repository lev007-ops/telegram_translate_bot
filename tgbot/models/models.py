import peewee as pw
from tgbot.config import load_config
from datetime import datetime

config = load_config()

db = pw.PostgresqlDatabase(config.db.database,
                           user=config.db.user,
                           password=config.db.password,
                           host=config.db.host,
                           autorollback=True
                           )


class BaseModel(pw.Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class User(BaseModel):
    telegram_id = pw.BigIntegerField()
    last_use = pw.DateTimeField(default=datetime.now())
    create_date = pw.DateTimeField(default=datetime.now())


def create_user(telegram_id: int):
    user, created = User.get_or_create(telegram_id=telegram_id)
    if not created:
        user.last_use = datetime.now()
        user.save()

