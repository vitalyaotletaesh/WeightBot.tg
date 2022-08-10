from aiogram import Bot, Dispatcher
from handlers.config import BOT_TOKEN

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)
