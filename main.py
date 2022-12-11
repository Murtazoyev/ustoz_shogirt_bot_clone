import logging
from typing import re
from Buttons.Buttons import startBtn, adminga_yuborish
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = '5749243532:AAG8G7JU6Sm42o_HX3BCe9iseECroCUtb6o'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class Anketa(StatesGroup):
    full_name = State()
    skills = State()
    phone_number = State()
    hudud = State()
    money = State()
    work = State()
    application = State()
    purpose = State()
    confirm = State()


@dp.(commands='start')
async def start(msg: types.Message):
    await msg.answer(f"""AssalomU alaykum
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!""", reply_markup=startBtn)


@dp.message_handler(text='Sherik kerak')
async def anketa(msg: types.Message):
    await msg.answer(f"""Sherik topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")
    await msg.answer(f"""Ism, familiyangizni kiriting?""")
    await Anketa.full_name.set()


@dp.message_handler(state=Anketa.full_name)
async def anketa(msg: types.Message, state: FSMContext):
    full_name = msg.text
    await state.update_data({
        'full_name': full_name
    })
    await msg.answer(f"""📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#""")
    await Anketa.skills.set()


@dp.message_handler(state=Anketa.skills)
async def anketa(msg: types.Message, state: FSMContext):
    skills = msg.text
    await state.update_data({
        'skills': skills
    })
    await msg.answer(f"""📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67""")
    await Anketa.phone_number.set()


@dp.message_handler(regexp='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', state=Anketa.phone_number)
async def anketa(msg: types.Message, state: FSMContext):
    phone_number = msg.text
    await state.update_data({
        'phone_number': phone_number
    })
    await msg.answer(f"""🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
    await Anketa.hudud.set()


@dp.message_handler(state=Anketa.hudud)
async def anketa(msg: types.Message, state: FSMContext):
    hudud = msg.text
    await state.update_data({
        'hudud': hudud
    })
    await msg.answer(f"""💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?""")
    await Anketa.money.set()


@dp.message_handler(state=Anketa.money)
async def anketa(msg: types.Message, state: FSMContext):
    money = msg.text
    await state.update_data({
        'money': money
    })
    await msg.answer(f"""👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba""")
    await Anketa.work.set()


@dp.message_handler(state=Anketa.work)
async def anketa(msg: types.Message, state: FSMContext):
    work = msg.text
    await state.update_data({
        'work': work
    })
    await msg.answer(f"""🕰 Murojaat qilish vaqti:

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00""")
    await Anketa.application.set()


@dp.message_handler(state=Anketa.application)
async def anketa(msg: types.Message, state: FSMContext):
    application = msg.text
    await state.update_data({
        'application': application
    })
    await msg.answer(f"""🔎 Maqsad:

Maqsadingizni qisqacha yozib bering.""")
    await Anketa.purpose.set()



@dp.message_handler(state=Anketa.purpose)
async def anketa(msg: types.Message, state: FSMContext):
    purpose = msg.text
    await state.update_data({
        'purpose': purpose
    })
    data = await state.get_data()

    skills = data['skills'].split()
    for i in skills:
        if i == "c++" or i == 'C++':
            print(i)
    natija = [f"#{item}" for item in skills]
    a = ' '.join(natija)

    await msg.answer(f"""Sherik kerak:

🏅 Sherik: {data['full_name']}
📚 Texnologiya: {data['skills']}
🇺🇿 Telegram: @{msg.from_user.username}
📞 Aloqa: {data['phone_number']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['money']}
👨🏻‍💻 Kasbi: {data['work']}
🕰 Murojaat qilish vaqti: {data['application']}
🔎 Maqsad: {data['purpose']}

#sherik {a} #{data['hudud']}""")
    await msg.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=adminga_yuborish)
    await Anketa.confirm.set()


@dp.message_handler(text="Ha", state=Anketa.confirm)
async def send_admin(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    skills = data['skills'].split()
    for i in skills:
        if i == "c++" or i == 'C++':
            print(i)
    natija = [f"#{item}" for item in skills]
    a = ' '.join(natija)
    await msg.answer("Anketandiz tekshirish uchun adminga jo'natildi", reply_markup=startBtn)
    await bot.send_message(chat_id=949677905, text=f"""
{msg.from_user.full_name}
    
Sherik kerak:

🏅 Sherik: {data['full_name']}
📚 Texnologiya: {data['skills']}
🇺🇿 Telegram: @{msg.from_user.username}
📞 Aloqa: {data['phone_number']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['money']}
👨🏻‍💻 Kasbi: {data['work']}
🕰 Murojaat qilish vaqti: {data['application']}
🔎 Maqsad: {data['purpose']}

#sherik {a} #{data['hudud']}""")
    await state.finish()
    await state.reset_state()


@dp.message_handler(text="Yo'q")
async def send_admin(msg: types.Message, state: FSMContext):
    await msg.delete()
    await msg.answer("Bosh Sahifaga o'tish", reply_markup=startBtn)
    await state.reset_state()

async def start_up(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Botni ishga tushurish'),
            types.BotCommand('help', 'Bot haqida'),
            types.BotCommand('exit', 'Botdan chiqish'),
        ]
    )

    await dp.bot.send_message(chat_id=949677905, text='Assalomu aleykum Bot ishga tushdi.')


executor.start_polling(dp, skip_updates=True, on_startup=start_up)
