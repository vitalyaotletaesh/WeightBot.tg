from aiogram import Bot, Dispatcher
from handlers.config import BOT_TOKEN
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
