from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💡 Kursga yozilish"),
            KeyboardButton(text="🧾 Kurs haqida"),
        ],
        [
            KeyboardButton(text="📩 Aloqa"),
            KeyboardButton(text="📍 Manzil"),
        ],
        [
            KeyboardButton(text="📚 Manbalar"),
            
        ],
[
            KeyboardButton(text="🔙 Ortga"),
        ],
    ],
    resize_keyboard=True
)


main_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💡 Записаться на курс"),
            KeyboardButton(text="🧾 О курсе"),
        ],
        [
            KeyboardButton(text="📩 Контакты"),
            KeyboardButton(text="📍 Наш адрес"),
        ],
        [
            KeyboardButton(text="📚 Источники"),
            
        ],
[
            KeyboardButton(text="🔙 Назад"),
        ],
    ],
    resize_keyboard=True
)


main_menu_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💡 Enroll in a course!"),
            KeyboardButton(text="🧾 About us"),
        ],
        [
            KeyboardButton(text="📩 Contacts"),
            KeyboardButton(text="📍 Location"),
        ],
        [
            KeyboardButton(text="📚 Sources"),
            
        ],
[
            KeyboardButton(text="🔙 Back"),
        ],
    ],
    resize_keyboard=True
)
