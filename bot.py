import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from tgbot.handlers.start import start_router
from tgbot.handlers.translate import translate_router

from tgbot.config import load_config
from tgbot.middlewares.config import ConfigMiddleware
from tgbot.services import broadcaster
from tgbot.models.models import db, User

logger = logging.getLogger(__name__)


async def on_startup(bot: Bot, admin_ids: list[int]):
    db.connect()
    db.create_tables([User])
    await broadcaster.broadcast(bot, admin_ids, "The bot has been launched!")


def register_global_middlewares(dp: Dispatcher, config):
    dp.message.outer_middleware(ConfigMiddleware(config))
    dp.callback_query.outer_middleware(ConfigMiddleware(config))


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
        '[%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)

    for router in [
        start_router,
        translate_router
    ]:
        dp.include_router(router)

    register_global_middlewares(dp, config)

    await on_startup(bot, config.tg_bot.admin_ids)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt):
        db.close()
        logger.error("The bot has been stopped!")
