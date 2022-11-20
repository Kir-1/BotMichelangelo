from aiogram.dispatcher.filters.state import StatesGroup, State


class ColorCorrectionState(StatesGroup):  # класс стадий для загрузки лут
    photo = State()
    lut = State()
