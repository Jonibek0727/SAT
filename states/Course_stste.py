from aiogram.dispatcher.filters.state import StatesGroup, State


class Course_registration(StatesGroup):
    fullname = State()
    contact = State()
    english_level = State()
    math_level = State()
