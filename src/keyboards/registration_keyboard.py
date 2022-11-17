from aiogram import types


def get_registration_keyboard() -> types.ReplyKeyboardMarkup:
    registration_keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True)
    registration_keyboard.add(types.KeyboardButton('Администратор'))
    registration_keyboard.add(types.KeyboardButton('Пользователь'))
    registration_keyboard.add(types.KeyboardButton('/cancel'))
    return registration_keyboard


def get_cancel_keyboard() -> types.ReplyKeyboardMarkup:
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True).add(types.KeyboardButton('/cancel'))
