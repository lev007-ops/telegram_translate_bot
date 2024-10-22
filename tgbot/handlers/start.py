from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from tgbot.models.models import create_user, User
from tgbot.filters.admin import AdminFilter
from aiogram.fsm.context import FSMContext
from tgbot.config import Config
from aiogram.types import Message, ReplyKeyboardRemove
from tgbot.misc.states import BroadcastStates
from tgbot.services.broadcaster import broadcast_telegram_message

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


@start_router.message(Command("broadcast"))
async def broadcast(message: Message, state: FSMContext, config: Config):
    if message.from_user.id not in config.tg_bot.admin_ids:
        return
    await state.clear()
    await message.answer("Введите текст рассылки (отмена - /start)",
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(BroadcastStates.input_message)


@start_router.message(BroadcastStates.input_message)
async def broadcast_input_message(message: Message,
                                  state: FSMContext, config: Config):
    if message.from_user.id not in config.tg_bot.admin_ids:
        return
    users = [int(user.telegram_id) for user in User.select()]
    await state.clear()
    await message.answer("Рассылка начата")
    await broadcast_telegram_message(users, message)
    await message.answer("Рассылка завершена. /start")
