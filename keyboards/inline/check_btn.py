
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


tekshir = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="✅ Yes", callback_data="send"),
		InlineKeyboardButton(text="❌ No", callback_data="wrong"),
	],
])

tekshir_ru = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="✅ Yes", callback_data="send_ru"),
		InlineKeyboardButton(text="❌ No", callback_data="wrong_ru"),
	],
])


tekshir_en = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="✅ Yes", callback_data="send_en"),
		InlineKeyboardButton(text="❌ No", callback_data="wrong_en"),
	],
])