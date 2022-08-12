from aiogram import types, Dispatcher

from handlers.admin import cm_start
from keyboards.client_kb import kb_client


async def commands_start(message: types.Message):
    await message.answer('Hello!', reply_markup=kb_client)


async def input_weight_command(message: types.Message):
    await cm_start(message)


async def create_chart_command(message: types.Message):
    await message.answer('chart')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(input_weight_command, commands=['Ввести_вес'])
    dp.register_message_handler(create_chart_command, commands=['Построить_график'])
