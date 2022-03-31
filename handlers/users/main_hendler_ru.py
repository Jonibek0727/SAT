import logging
from data.config import GROUP_CHAT_ID
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from loader import dp, bot
from keyboards.default.main_btn_uz import main_menu_ru
from keyboards.default.lan_btn import menulan
from keyboards.default.contact_btn import contact_Btn
from states.Course_state_ru import Course_registration_ru
from keyboards.default.english_level import english_l_btn
from keyboards.default.math import math_l_btn_ru
from keyboards.inline.check_btn import tekshir_ru
import re
from datetime import datetime




PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'




@dp.message_handler(text = "🇷🇺 RU")
async def create_post(message: Message):
    await message.answer("<b>🇺🇿 SATashkent School </b>SATashkent School – является одним из первых официальных школ в Ташкенте, которая обучает студентов по программе SAT (Scholastic Aptitude Test). Экзамен SAT требуется от всех, кто хочет учиться в колледже США с щедрой стипендией. Поэтому, мы хотели помочь этим людям в реализации их устремлений. \nНаша школа ориентирована исключительно на результаты и качество.", reply_markup=main_menu_ru)


@dp.message_handler(text ='🔙 Назад')
async def bot_start(message: types.Message):
    await message.answer(f"Choose your language!", reply_markup=menulan)


@dp.message_handler(text ='💡 Записаться на курс')
async def bot_start(message: types.Message):
    await message.answer("Введите свои личные данные для регистрации.")
    await message.answer("Ваше имя и фамилия", reply_markup=ReplyKeyboardRemove())
    await Course_registration_ru.fullname.set()


@dp.message_handler(state=Course_registration_ru.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"name": fullname}
    )

    await message.answer("Введите свой номер телефона.", reply_markup=contact_Btn)

    await Course_registration_ru.next()

@dp.message_handler(state=Course_registration_ru.contact, content_types="contact")
async def answer_fullname(message: types.Message, state: FSMContext):
    contact = message

    if contact.contact:
        # print(phone_num.contact)
        if re.search(PHONE_NUM, contact.contact.phone_number):
            await state.update_data(
                {"phone_number": contact.contact.phone_number}
            )
            await message.answer("Ваш уровень английского", reply_markup=english_l_btn)
            await Course_registration_ru.next()

    elif 'text' in contact:
        if re.search(PHONE_NUM, contact.text):

            await state.update_data(
                {"phone_number": contact.text}
            )
            await message.answer("Ваш уровень английского", reply_markup=english_l_btn)
            await Course_registration_ru.next()
        else:
            await message.answer("❌ Вы ввели неправильный номер. , \nПожалуйста, введите снова!")
            await Course_registration_ru.contact.set()



    else:
        await message.answer("❌ Вы ввели неправильный номер. , \nПожалуйста, введите снова!")
        await Course_registration_ru.contact.set()

@dp.message_handler(state=Course_registration_ru.english_level)
async def answer_fullname(message: types.Message, state: FSMContext):
    english = message.text
    await state.update_data(
        {"english": english}
    )
    await message.answer("Ваш уровень по математике", reply_markup=math_l_btn_ru)

    await Course_registration_ru.next()

@dp.message_handler(state=Course_registration_ru.math_level)
async def answer_fullname(message: types.Message, state: FSMContext):
    math = message.text
    await state.update_data(
        {"math": math}
    )


    data = await state.get_data()
    name = data.get("name")
    phone_number = data.get("phone_number")
    english = data.get("english")
    math = data.get("math")

    today = datetime.today()
    day = f"{today.strftime('%d')}/{today.strftime('%m')}/{today.strftime('%y')}"

    global _ru

    _ru = "📌 Ваша личная информация! \n\n"
    _ru += f"<b>Full name</b>: {name}\n"
    _ru += f"<b>Phone Number</b>:{phone_number}\n"
    _ru += f"<b>English level</b>:{english}\n"
    _ru += f"<b>Math level</b>:{math}\n"
    _ru += f"<b>Date</b> :{day}\n"
    await message.answer(_ru)
    await state.finish()
    await message.answer("Вы отправите заявку?", reply_markup=tekshir_ru)


@dp.callback_query_handler(text="send_ru")
async def arizani_yuborish(call: CallbackQuery):
   
    await call.message.delete()
    await bot.send_message(GROUP_CHAT_ID, _ru)

    await call.message.answer("✅ Ваша заявка отправлена!\n☎️Мы свяжемся с вами в ближайшее время", reply_markup=main_menu_ru)
    await call.answer(cache_time=30)
    await call.answer()


@dp.callback_query_handler(text="wrong_ru")
async def arizani_bekor_qilish(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("❌ Ваша заявка была отменена!", reply_markup=main_menu_ru)
    await call.answer(cache_time=30)
    await call.answer()

@dp.message_handler(text ='📩 Контакты')
async def bot_start(message: types.Message):
    await message.answer("Чтобы связаться со школой SATashkent:\n\n📞 +998919253036\n\n<a href='https://t.me/satashkent_admin'>Telegram</a>")


@dp.message_handler(text ='📍 Наш адрес')
async def bot_start(message: types.Message):
    await message.answer("Location: M Shahriston, ICT Academy\nContact : +998919253036")
    await message.answer_location(latitude=41.35426269309694, longitude=69.28861938201761)

@dp.message_handler(text ='🧾 О курсе')
async def bot_start(message: types.Message):
    await message.answer("Добро пожаловать в <b>SATashkent School!</b>\n\n📌У нас есть 2 вида курсов SAT:\n - Senior Course\n-  Junior Course\nSATashkent School предлагает каждому студенту:\n\n • Система Support Teacher \n • 6 дневных занятий в неделю \n• Максимум 12 учеников в классе  \n • Консультации по подаче заявления за границу\n• Нетворкинг с выпускниками! \n• Система организованных и индивидуальных домашних заданий (с искусственным интеллектом) \n\nВсе в одном месте!😍  ")



@dp.message_handler(text ='📚 Источники')
async def bot_start(message: types.Message):
    await message.answer("""Good day to everybody!

‼️Welcome to the SAT|English materials channel with no limits. All new|old English books, subjects, and other resources may be found here. This channel was created under the @satashkent School

📌This channel's goal is to assist people in improving their SAT scores and enrolling in world-class institutions. We want that even the children of those who live on the edges of Uzbekistan have unlimited access to materials. This channel is made only for humans!

1.0 Reading Comprehension Materials
1.2 Literature Reading Materials 

<a href="https://t.me/c/1778480012/564">9-10 Class</a>
<a href="https://t.me/c/1778480012/625">11-12 Class</a> 
1.3 Science Reading Materials 
<a href = "https://t.me/c/1778480012/674">9-10 Class</a>
<a href = "https://t.me/c/1778480012/687">11-12 Class</a> 
1.4 Social Science Reading Materials
<a href = "https://t.me/c/1778480012/702">9-10 Class</a>
<a href = "https://t.me/c/1778480012/711" >11-12 Class</a> 

1.5 Great Global Conversations (History)
<a href = "https://t.me/c/1778480012/735">All here</a>

1.6 Founding Documents (History&Science
<a href = "https://t.me/c/1778480012/725">9-10 Class</a>
<a href = "https://t.me/c/1778480012/731">11-12 Class</a>

2.0 Magazines
<a href = "https://t.me/c/1778480012/910">2.1 New Scientist</a>
<a href = "https://t.me/c/1778480012/836">2.3 National Geographic</a>
<a href = "https://t.me/c/1778480012/897">2.4 Scientific American</a>
<a href = "https://t.me/c/1778480012/910">2.5 The Atlantic</a>
<a href = "https://t.me/c/1778480012/784">2.6 The Economist</a>
<a href = "https://t.me/c/1778480012/979" >2.7 Time Magazine</a>
<a href = "https://t.me/c/1778480012/1000">2.8 The Wall Street Journal</a>

<a href = "https://t.me/c/1778480012/1114">3.0 SAT Full Books</a>

4.0 SAT section Based Books
<a href = "https://t.me/c/1778480012/1027">Writing</a>
<a href = "https://t.me/c/1778480012/1065">Math</a>
<a href = "https://t.me/c/1778480012/1089">Reading</a>

<a href = "https://t.me/c/1778480012/1007">5.0 SAT Vocabulary Books</a>

6.0 SAT Practise Tests
<a href = "https://t.me/c/1778480012/1127">Official College Board 10 Tests</a>
<a href = "https://t.me/c/1778480012/1124">Real SAT exam tests from 2017- 2021</a>

7.0 Others

❕To make it easy to follow, you can use map above!

📕New updates will be added throughout the development of this channel. Now, you can get what is here!

‼️Remember, all the information, documents, books must be used for educational purposes. All the information, books, documents that are widely available in Google. 

📂Source of many materials: Google.com and <a href = "https://t.me/SAT_FILES">SAT Files</a>

Link to join: https://t.me/+QeAkLfpPBd9jZGRi

<a href = "https://t.me/satashkent">SATashkent School!</a>""")