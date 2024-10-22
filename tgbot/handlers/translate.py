from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message

from tgbot.services.translator import translate
from tgbot.services.yandex_translate import ya_translate
from tgbot.services.yandex_detector import ya_detect
from tgbot.services.get_ya_token import get_iam_token
from tgbot.models.models import create_user

translate_router = Router()


@translate_router.message(Text)
async def user_start(message: Message):
    await message.reply(
        "Принял твой текст, скоро отправлю перевод:\n\n--\n\n"
        "Синең текстыңны кабул иттем, тиздән тәрҗемә җибәрәчәкмен:"
    )
    text = message.text
    error_text = (
        "Ошибка перевода, попробуйте в другой раз\n\n--\n\n"
        "Тәрҗемә хатасы, бүтән тапкыр карагыз\n\n"
        "Error code: ")
    iam_token = await get_iam_token()
    if not iam_token:
        await message.answer(f"{error_text} where is my damn token")
    lang = await ya_detect(text, iam_token)

    if not lang:
        await message.answer(f"{error_text} dude, just tell me the language")
        return
    if lang in ("ru", "en"):
        text = await ya_translate(lang, message.text,
                                  iam_token)
        if not text:
            await message.answer(f"{error_text} give me that darn translation")
            return
        await message.answer(text)
    arab_text = translate(text)
    await message.answer(arab_text)
    create_user(message.from_user.id)
