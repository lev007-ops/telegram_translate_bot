from aiogram.fsm.state import State, StatesGroup


class BroadcastStates(StatesGroup):
    input_message = State()
    confirm = State()
