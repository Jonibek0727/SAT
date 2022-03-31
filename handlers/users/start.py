from email import message
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.lan_btn import menulan
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}!\nChoose your language!", reply_markup=menulan)
    
   