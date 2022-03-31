from aiogram.dispatcher.filters.state import StatesGroup, State


class Course_registration_en(StatesGroup):
    fullname = State()
    contact = State()
    english_level = State()
    math_level = State()
