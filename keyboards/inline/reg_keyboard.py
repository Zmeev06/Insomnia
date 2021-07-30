from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data import config

registration= InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Пройти регистрацию', url=config.BOT_START_URL)
    ]
])