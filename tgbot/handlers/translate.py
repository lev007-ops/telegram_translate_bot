from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message

from tgbot.services.translator import translate

translate_router = Router()


@translate_router.message(Text)
async def user_start(message: Message):
    await message.reply(
        "Принял твой текст, скоро отправлю перевод:\n\n--\n\n"
        "Синең текстыңны кабул иттем, тиздән тәрҗемә җибәрәчәкмен:"
    )
    text = translate(message.text)
    await message.answer(text)
