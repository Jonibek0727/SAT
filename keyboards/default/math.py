from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

math_l_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Boshlang'ich"),
            KeyboardButton(text="O'rta"),
        ],
        [
            KeyboardButton(text="A'lo"),
        ],

    ],
    resize_keyboard=True
)


math_l_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Начальный"),
            KeyboardButton(text="Средний"),
        ],
        [
            KeyboardButton(text="Высший"),
        ],

    ],
    resize_keyboard=True
)

math_l_btn_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Beginner"),
            KeyboardButton(text="Elementary"),
        ],
        [
            KeyboardButton(text="Intermediate"),
        ],

    ],
    resize_keyboard=True
)
