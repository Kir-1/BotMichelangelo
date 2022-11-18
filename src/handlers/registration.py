from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from src.keyboards.admin_keyboard import get_admin_keyboard
from src.keyboards.user_keyboard import get_user_keyboard
from src.main import bot, dp
from src.services.mongodb import AdminsDB, UsersDB
from src.keyboards.registration_keyboard import get_registration_keyboard, get_cancel_keyboard
from src.states.state_registration_admin import AdminRegistrationState


# выполняется при вызове команды старт
@dp.message_handler(commands=['start'], state=None)
async def start_command(message: types.Message) -> None:
    if AdminsDB.collection.find_one({'_id': message.from_user.id}) is not None:
        await message.answer("Вы Администратор")  # добавить возможности Админу

    elif UsersDB.collection.find_one({'_id': message.from_user.id}) is not None:
        await message.answer("Вы Пользователь")  # добавить возможности пользователю

    else:
        await bot.send_message(chat_id=message.from_user.id, text="Вы ещё не зарегистрированы!\n Выберите кто вы.",
                               reply_markup=get_registration_keyboard())


# выполняется при вызове команды cancel
@dp.message_handler(commands=['cancel'], state='*')
async def cancel_command(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if AdminsDB.collection.find_one({'_id': message.from_user.id}) is not None:
        await message.answer("Вы Администратор")  # добавить возможности Админу
        await state.finish()
        return
    elif UsersDB.collection.find_one({'_id': message.from_user.id}) is not None:
        await message.answer("Вы Пользователь")  # добавить возможности пользователю
        await state.finish()
        return
    elif current_state is None:
        await message.answer("Скажи когда будешь готов", reply_markup=get_registration_keyboard())
        return




# начало регистрации Админа
@dp.message_handler(Text(equals="Администратор", ignore_case=True), state=None)
async def start_registration_admin(message: types.Message, state: FSMContext) -> None:
    await AdminRegistrationState.password.set()
    await message.answer("Введите пароль:", reply_markup=get_cancel_keyboard())


# проверка пароля
@dp.message_handler(lambda message: message.text, state=AdminRegistrationState.password)
async def check_password(message: types.Message, state: FSMContext) -> None:
    if message.text == AdminsDB.password:
        AdminsDB.collection.insert_one({"_id": message.from_user.id, "_username": message.from_user.username})
        await message.answer("Вы Администратор", reply_markup=get_admin_keyboard())  # добавить возможности Админу
        await state.finish()
    else:
        await message.answer("Пароль неверный")


# начало регистрации Пользователя
@dp.message_handler(Text(equals="Пользователь", ignore_case=True), state=None)
async def start_registration_admin(message: types.Message, state: FSMContext) -> None:
    UsersDB.collection.insert_one({"_id": message.from_user.id, "_username": message.from_user.username})
    await message.answer("Вы Пользователь", reply_markup=get_user_keyboard())  # добавить возможности Админу
