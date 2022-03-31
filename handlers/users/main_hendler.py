import logging
from data.config import GROUP_CHAT_ID
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from loader import dp, bot
from keyboards.default.main_btn_uz import main_menu
from keyboards.default.lan_btn import menulan
from keyboards.default.contact_btn import contact_Btn
from states.Course_stste import Course_registration
from keyboards.default.english_level import english_l_btn
from keyboards.default.math import math_l_btn
from keyboards.inline.check_btn import tekshir
import re
from datetime import datetime




PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'




@dp.message_handler(text = "🇺🇿 UZ")
async def create_post(message: Message):
    await message.answer("<b>🇺🇿 SATashkent </b>maktabi bu - SAT (Scholastic Aptitude Test) imtihoniga tayyorlovchi,  Toshkentdagi ilk rasmiy maktablardan biri. SAT imtihoni AQSh universitetlarida grant asosida o'qishni istagan har bir kishidan talab qilinadi. Shunday ekan, biz sizga maqsadlaringizni amalga oshirishda yordam beramiz.", reply_markup=main_menu)


@dp.message_handler(text ='🔙 Ortga')
async def bot_start(message: types.Message):
    await message.answer(f"Choose your language!", reply_markup=menulan)


@dp.message_handler(text ='💡 Kursga yozilish')
async def bot_start(message: types.Message):
    await message.answer("Ro'yxatdan otish uchun shaxsiy malumotlarizni kiriting.")
    await message.answer("To'liq Ism va Familyangiz?", reply_markup=ReplyKeyboardRemove())
    await Course_registration.fullname.set()


@dp.message_handler(state=Course_registration.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"name": fullname}
    )

    await message.answer("Telefon raqamingizni kiriting.", reply_markup=contact_Btn)

    await Course_registration.next()

@dp.message_handler(state=Course_registration.contact, content_types="contact")
async def answer_fullname(message: types.Message, state: FSMContext):
    contact = message

    if contact.contact:
        # print(phone_num.contact)
        if re.search(PHONE_NUM, contact.contact.phone_number):
            await state.update_data(
                {"phone_number": contact.contact.phone_number}
            )
            await message.answer("Ingliz tili darajangiz", reply_markup=english_l_btn)
            await Course_registration.next()

    elif 'text' in contact:
        if re.search(PHONE_NUM, contact.text):

            await state.update_data(
                {"phone_number": contact.text}
            )
            await message.answer("Ingliz tili darajangiz", reply_markup=english_l_btn)
            await Course_registration.next()
        else:
            await message.answer("❌ Noto'g'ri raqam terdingiz!, \nQaytadan kiriting!")
            await Course_registration.contact.set()



    else:
        await message.answer("❌ Noto'g'ri raqam terdingiz!, \nQaytadan kiriting!")
        await Course_registration.contact.set()

@dp.message_handler(state=Course_registration.english_level)
async def answer_fullname(message: types.Message, state: FSMContext):
    english = message.text
    await state.update_data(
        {"english": english}
    )
    await message.answer("Matematika bilim darajangiz", reply_markup=math_l_btn)

    await Course_registration.next()

@dp.message_handler(state=Course_registration.math_level)
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

    global _uz

    _uz = "📌 Shaxsiy ma'lumotlaringiz! \n\n"
    _uz += f"<b>Full name</b>: {name}\n"
    _uz += f"<b>Phone Number</b>:{phone_number}\n"
    _uz += f"<b>English level</b>:{english}\n"
    _uz += f"<b>Math level</b>:{math}\n"
    _uz += f"<b>Date</b> :{day}\n"
    await message.answer(_uz)
    await state.finish()
    await message.answer("Arizani yuborasizmi?", reply_markup=tekshir)


@dp.callback_query_handler(text="send")
async def arizani_yuborish(call: CallbackQuery):
    await call.message.delete()
    await bot.send_message(GROUP_CHAT_ID, _uz)

    await call.message.answer("✅ Arizangiz yuborildi!\n☎️Siz bilan tez orada bog'lanamiz", reply_markup=main_menu)
    await call.answer(cache_time=30)
    await call.answer()


@dp.callback_query_handler(text="wrong")
async def arizani_bekor_qilish(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("❌ Arizangiz bekor qilindi!", reply_markup=main_menu)
    await call.answer(cache_time=30)
    await call.answer()

@dp.message_handler(text ='📩 Aloqa')
async def bot_start(message: types.Message):
    await message.answer("SATashkent School'ga bog'lanish uchun:\n\n📞 +998919253036\n\n<a href='https://t.me/satashkent_admin'>Telegram</a>")


@dp.message_handler(text ='📍 Manzil')
async def bot_start(message: types.Message):
    await message.answer("Location: M Shahriston, ICT Academy\nContact : +998919253036")
    await message.answer_location(latitude=41.35426269309694, longitude=69.28861938201761)

@dp.message_handler(text ='🧾 Kurs haqida')
async def bot_start(message: types.Message):
    await message.answer("<b>SATashkent</b> School xush kelibsiz!\n\n📌Bizda SAT kurslarining 2 turi mavjud:\n - Senior Course\n-  Junior Course\nSATashkent School har bir talaba uchun quyidagi qulayliklarni yaratadi:\n\n • Support Teacher xizmati\n • Haftada 6 kunlik darslar \n• Bir sinfda maksimal 12 talaba \n • Chet elga hujjat topshirish bo'yicha maslahatlar\n• Bitiruvchilar bilan aloqa o'rnatish! \n• Tartibli va Individual uy vazifalari tizimi (AI bilan) \n\nBularning hammasi bir joyda!😍  ")




@dp.message_handler(text ='📚 Manbalar')
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



