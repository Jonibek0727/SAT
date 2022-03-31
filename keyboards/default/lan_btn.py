from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menulan = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 UZ"),
        ],
        [
            KeyboardButton(text="🇷🇺 RU"),
            KeyboardButton(text="🇺🇸 EN"),
        ],
    ],
    resize_keyboard=True
)
