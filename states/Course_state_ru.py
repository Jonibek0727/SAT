from aiogram.dispatcher.filters.state import StatesGroup, State


class Course_registration_ru(StatesGroup):
    fullname = State()
    contact = State()
    english_level = State()
    math_level = State()
