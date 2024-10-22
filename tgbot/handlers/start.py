from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from tgbot.models.models import create_user, User
from tgbot.filters.admin import AdminFilter

start_router = Router()


@start_router.message(CommandStart())
async def user_start(message: Message):
    await message.answer(
        "Ас-саляму алейкум! Данный бот предназначен для "
        "транслитерации татарских текстов с кириллицы на арабицу. "
        "Пришлите свой текст. Разработчик бота: @lev_man\n\n--\n\n"
        "Әс-сәләм әлейкум! Бу бот татар текстларын кириллицадан"
        "гарәпчәгә транслитерацияләү өчен билгеләнгән. "
        "Текстыгызны җибәрегез. Ботны эшләүче: @lev_man")
    create_user(message.from_user.id)


@start_router.message(Command("count_users"), AdminFilter())
async def count_users(message: Message):
    users = len(User.filter())
    await message.answer(f"Всего пользователей: {users}")
