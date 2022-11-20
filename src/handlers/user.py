import typing

import pillow_lut
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from src.keyboards.admin_keyboard import get_admin_keyboard
from src.keyboards.registration_keyboard import get_cancel_keyboard
from src.main import dp
from src.main import bot
from src.services.mongodb import LutDB
from src.states.state_color_correction import ColorCorrectionState


# начало цветокоррекции
@dp.message_handler(Text(equals="Цветокоррекция", ignore_case=True), state=None)
async def start_color_correction(message: types.Message, state: FSMContext) -> None:
    await ColorCorrectionState.photo.set()
    await message.answer("Отправьте фото для цветокоррекции", reply_markup=get_cancel_keyboard())


@dp.message_handler(content_types=['photo'], state=ColorCorrectionState.photo)
async def photo_choose(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    for element in LutDB.collection.find().sort('_id', 1):
        await bot.send_photo(message.from_user.id, photo=element['preview'], caption=element['_id'])
    await message.answer("Теперь выберите какую цветокоррекцию вы хотите", reply_markup=get_cancel_keyboard())
    await ColorCorrectionState.next()


@dp.message_handler(lambda message: message.text.isdigit(), state=ColorCorrectionState.lut)
async def lut_choose(message: types.Message, state: FSMContext) -> None:
    element_db = LutDB.collection.find_one({"_id": int(message.text)})
    if element_db is not None:
        file = await bot.get_file(element_db['lut_file'])
        file_path = file.file_path
        result = await bot.download_file(file_path, "lut.cube")
        a = pillow_lut.load_cube_file('lut.cube')
        print(a)
    else:
        await message.answer("Такой цветокоррекции нет")
