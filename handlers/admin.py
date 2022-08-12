from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher


class FSMAdmin(StatesGroup):
    date = State()
    weight = State()


async def cm_start(message: types.Message):
    await FSMAdmin.date.set()
    await message.reply('Введи дату в формате \'30.03.2002\'')


async def load_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await FSMAdmin.next()
    await message.reply('Теперь введи вес')


async def load_weight(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['weight'] = message.text
    # тест
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()


# Выход из состояния
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Ввести_вес'], state=None)
    dp.register_message_handler(load_date, state=FSMAdmin.date)
    dp.register_message_handler(load_weight, state=FSMAdmin.weight)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
