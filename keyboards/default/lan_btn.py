from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menulan = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="πΊπΏ UZ"),
        ],
        [
            KeyboardButton(text="π·πΊ RU"),
            KeyboardButton(text="πΊπΈ EN"),
        ],
    ],
    resize_keyboard=True
)
