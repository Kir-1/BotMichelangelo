from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from src.keyboards.admin_keyboard import get_admin_keyboard
from src.keyboards.registration_keyboard import get_cancel_keyboard
from src.main import dp
from src.services.mongodb import LutDB
from src.states.state_load_lut import LoadLutState


# начало загрузки лут
@dp.message_handler(Text(equals="Загрузить LUT", ignore_case=True), state=None)
async def start_load_lut(message: types.Message, state: FSMContext) -> None:
    await LoadLutState.lut.set()
    await message.answer("Отправьте LUT файл с расщирением .cube", reply_markup=get_cancel_keyboard())


@dp.message_handler(content_types=['document'], state=LoadLutState.lut)
async def load_lut_cube(message: types.Message, state: FSMContext) -> None:
    if message.document.file_name[-4:-1] == 'cub':
        async with state.proxy() as data:
            data['lut_file'] = message.document.file_id
            data['format'] = '.cube'
            data['name'] = message.document.file_name
        await message.answer("Загрузите превью для LUT", reply_markup=get_cancel_keyboard())
        await LoadLutState.next()
    else:
        await message.answer("Не тот формат")


@dp.message_handler(content_types=['photo'], state=LoadLutState.preview_lut)
async def load_lut_preview(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['preview'] = message.photo[0].file_id
        count = 0
        for element in LutDB.collection.find().sort('_id', -1):
            count = element['_id']

        LutDB.collection.insert_one({"_id": count+1, "lut_file": data['lut_file'], "preview": data['preview'], "name": data['name']})

    await message.answer("LUT успешно загружен", reply_markup=get_admin_keyboard())
    await state.finish()
