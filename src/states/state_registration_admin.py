from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminRegistrationState(StatesGroup):  # класс стадий для регистрации
    password = State()
