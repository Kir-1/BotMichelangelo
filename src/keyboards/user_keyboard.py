from aiogram import types


def get_user_keyboard() -> types.ReplyKeyboardMarkup:
    user_keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True)
    user_keyboard.add(types.KeyboardButton('Цветокорекция'))
    user_keyboard.add(types.KeyboardButton('Другое'))
    return user_keyboard
