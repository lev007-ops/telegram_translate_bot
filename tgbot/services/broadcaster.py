import asyncio
import logging

from aiogram import Bot
from aiogram import exceptions
from aiogram.types import Message


async def send_message(bot: Bot, user_id, text: str,
                       disable_notification: bool = False) -> bool:
    try:
        await bot.send_message(user_id, text,
                               disable_notification=disable_notification)
    except exceptions.TelegramForbiddenError:
        logging.error(f"Target [ID:{user_id}]: got TelegramForbiddenError")
    except exceptions.TelegramRetryAfter as e:
        logging.error(f"Target [ID:{user_id}]: Flood limit is exceeded. "
                      f"Sleep {e.retry_after} seconds.")
        await asyncio.sleep(e.retry_after)
        return await send_message(bot, user_id, text)  # Recursive call
    except exceptions.TelegramAPIError:
        logging.exception(f"Target [ID:{user_id}]: failed")
    else:
        logging.info(f"Target [ID:{user_id}]: success")
        return True
    return False


async def send_telegram_message(user_id, message: Message,
                       disable_notification: bool = False) -> bool:
    try:
        await message.copy_to(user_id, disable_notification=disable_notification)
    except exceptions.TelegramForbiddenError:
        logging.error(f"Target [ID:{user_id}]: got TelegramForbiddenError")
    except exceptions.TelegramRetryAfter as e:
        logging.error(f"Target [ID:{user_id}]: Flood limit is exceeded. "
                      f"Sleep {e.retry_after} seconds.")
        await asyncio.sleep(e.retry_after)
        return await send_telegram_message(user_id, message)  # Recursive call
    except exceptions.TelegramAPIError:
        logging.exception(f"Target [ID:{user_id}]: failed")
    else:
        logging.info(f"Target [ID:{user_id}]: success")
        return True
    return False


async def broadcast(bot, users, text) -> int:
    """
    Simple broadcaster
    :return: Count of messages
    """
    count = 0
    try:
        for user_id in users:
            if await send_message(bot, user_id, text):
                count += 1
            # 20 messages per second (Limit: 30 messages per second)
            await asyncio.sleep(0.05)
    finally:
        logging.info(f"{count} messages successful sent.")

    return count


async def broadcast_telegram_message(users, message: Message):
    count = 0
    try:
        for user_id in users:
            if await send_telegram_message(user_id, message):
                count += 1
            # 20 messages per second (Limit: 30 messages per second)
            await asyncio.sleep(0.05)
    finally:
        logging.info(f"{count} messages successful sent.")

    return count