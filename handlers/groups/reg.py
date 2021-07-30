from aiogram import types
from aiogram.types import Message
from loader import dp
from keyboards.inline.reg_keyboard import registration

@dp.message_handler(content_types=["new_chat_members"])
async def capcha(message: types.Message):
	user_id= message.from_user.id
	name=message.from_user.full_name
	await message.answer(f'Привет <a href="tg://user?id={user_id}">{name}</a>! 👋\
			\nВ целях защиты чата от спама и соблюдения возрастных ограничений тебе запрещено писать сообщения, пока не пройдешь регистрацию.',
            reply_markup=registration)