from aiogram import executor
from create_bot import dp, bot
from handlers.config import admin_id
from handlers import client, admin, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)

async def on_startup(dispatcher):
    await bot.send_message(chat_id=admin_id, text='Бот запущен.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
