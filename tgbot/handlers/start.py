from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

start_router = Router()


@start_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply(
        "Ас-саляму алейкум! Данный бот предназначен для "
        "транслитерации татарских текстов с кириллицы на арабицу. "
        "Пришлите свой текст. Разработчик бота: @lev_man\n\n--\n\n"
        "Әс-сәләм әлейкум! Бу бот татар текстларын кириллицадан"
        "гарәпчәгә транслитерацияләү өчен билгеләнгән. "
        "Текстыгызны җибәрегез. Ботны эшләүче: @lev_man")
