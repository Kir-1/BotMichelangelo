from aiogram.dispatcher.filters.state import StatesGroup, State


class LoadLutState(StatesGroup):  # класс стадий для загрузки лут
    lut = State()
    preview_lut = State()
