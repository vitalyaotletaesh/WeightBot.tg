from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb1 = KeyboardButton('/Ввести_вес')
kb2 = KeyboardButton('/Построить_график')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(kb1).add(kb2)
