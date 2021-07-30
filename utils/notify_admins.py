import logging

from aiogram import Dispatcher

from data.config import GLAV_ADMINS

async def on_startup_notify(dp: Dispatcher):
    for admin in GLAV_ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")
        
        except Exception as err:
            logging.exception(err)
