from aiogram import types


def get_admin_keyboard() -> types.ReplyKeyboardMarkup:
    admin_keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True)
    admin_keyboard.add(types.KeyboardButton('Загрузить LUT'))
    admin_keyboard.add(types.KeyboardButton('Другое'))
    return admin_keyboard
