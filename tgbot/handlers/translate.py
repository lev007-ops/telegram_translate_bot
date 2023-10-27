from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message

from tgbot.services.translator import translate
from tgbot.services.yandex_translate import ya_translate
from tgbot.services.yandex_detector import ya_detect

translate_router = Router()


@translate_router.message(Text)
async def user_start(message: Message):
    await message.reply(
        "Принял твой текст, скоро отправлю перевод:\n\n--\n\n"
        "Синең текстыңны кабул иттем, тиздән тәрҗемә җибәрәчәкмен:"
    )
    text = message.text
    lang = await ya_detect(text)
    error_text = ("Ошибка перевода, попробуйте в другой раз\n\n"
                  "Тәрҗемә хатасы, бүтән тапкыр карагыз")
    if not lang:
        await message.answer(error_text)
        return
    if lang == "ru":
        text = await ya_translate("ru", message.text)
        if not text:
            await message.answer(error_text)
            return
    text = translate(text)
    await message.answer(text)
