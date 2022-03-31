from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

english_l_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pre-Intermediate"),
            KeyboardButton(text="Intermediate"),
        ],
[
            KeyboardButton(text="Upper-Intermediate"),
            KeyboardButton(text="Advanced"),
        ],

    ],
    resize_keyboard=True
)
