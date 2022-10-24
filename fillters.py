# import logging
#
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram import filters
#
# API_TOKEN = '5749243532:AAG8G7JU6Sm42o_HX3BCe9iseECroCUtb6o'
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
#
# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
#
#
#
#
#
# admins = [949677905]
# words = [
#     'Axmoq', 'Jinni', 'Yaramas', 'Mol', 'Eshshak', 'Iflos'
# ]
#
#
#
#
# @dp.message_handler(text=words)
# async def words_text(msg: types.Message):
#     await msg.reply(f"O'zing {msg.text}")
#     await bot.send_message(chat_id=949677905, text=f"Sizga so'kindi {msg.from_user.username} ----- {msg.text} deb")\
#
#
#
#
#
# @dp.message_handler(text=["Assalom", "Assalomu aleykum", 'Salom'])
# async def send_message(msg: types.Message):
#     await msg.answer('Assalomu aleykum va Rahmatullohu va Barokatuhu')
#
#
#
#
#
#
#
# @dp.message_handler(regexp='^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$')
# async def send_alert(msg: types.Message):
#     await msg.answer('to\'g\'ri password')
#
#
#
#
#
#
#
#
#
#
# chat_id = [949677905]
#
#
# @dp.message_handler(chat_id=chat_id, text='Salom')
# async def seng_message(msg: types.Message):
#     await msg.answer("Xush kelibsiz Admin")
#
#
#
#
#
#
#
#
#
# @dp.message_handler(content_types='photo')
# async def seng_message(msg: types.Message):
#     await msg.answer("iltimos rasm yubormang")
#
#
#
#
#
#
#
#
#
#
# @dp.message_handler(hashtags='Salom')  # ( #Salom)
# async def hashTag(msg: types.Message):
#     await msg.answer('Salom hashtagi')
#
#
#
#
#
#
#
#
#
#
# # @dp.message_handler(cashtags='$euro')  # ($euro)
# # async def hashTag(msg: types.Message):
# #     await msg.answer("1 euro 10000 so'm")
#
#
#
#
#
#
#
#
#
#
#
#
#
# @dp.message_handler(content_types=types.ContentType.STICKER)
# async def seng_message(msg: types.Message):
#     await msg.answer("iltimos Sticker yubormang")
#
#
#
#
#
#
#
#
#
#
#
# async def start_up(dp):
#     await dp.bot.set_my_commands(
#         [
#             types.BotCommand('start', 'Botni ishga tushurish'),
#             types.BotCommand('help', 'Bot haqida'),
#             types.BotCommand('exit', 'Botdan chiqish'),
#         ]
#     )
#
#     await dp.bot.send_message(chat_id=949677905, text='Assalomu aleykum Bot ishga tushdi.')
#
#
# executor.start_polling(dp, skip_updates=True, on_startup=start_up)
















#                                                    State lar bilan ishlash
#
# class AnketaInfo(StatesGroup):
#     firstName = State()
#     lastName = State()
#     age = State()
#
#
# @dp.message_handler(text='Anketa')
# async def anketa(msg: types.Message, state: FSMContext):
#     await msg.answer('Iltimos ismingizni kiriting')
#     await AnketaInfo.firstName.set()
#
#
# @dp.message_handler(state=AnketaInfo.firstName)
# async def anketa(msg: types.Message, state: FSMContext):
#     await state.update_data({
#         'firstName': msg.text
#     })
#     await msg.answer('Iltimos familiyangizni kiriting')
#     await AnketaInfo.lastName.set()
#
#
# @dp.message_handler(state=AnketaInfo.lastName)
# async def anketa(msg: types.Message, state: FSMContext):
#     await state.update_data({
#         'lastName': msg.text
#     })
#     await msg.answer('Iltimos yoshingizni kiriting kiriting')
#     await AnketaInfo.age.set()
#
#
# @dp.message_handler(state=AnketaInfo.age)
# async def anketa(msg: types.Message, state: FSMContext):
#     await state.update_data({
#         'age': msg.text
#     })
#     data = await state.get_data()
#     await msg.answer('Ma\'lumotlaringiz uchun katta rahmat.')
#     await msg.answer(f"User ma'lumotlri \n"
#                      f"ismi: {data['firstName']} \n"
#                      f"familiyasi: {data['lastName']} \n"
#                      f"age: {data['age']}"
#                      )
#
#     await state.finish()






#
#
# @dp.message_handler(commands='start')
# async def start_def(msg: types.Message):
#     await msg.answer(f"""Assalom alaykum دِلشَدْ مُرْتَازَيِفْ
# UstozShogird kanalining test rasmiy botiga xush kelibsiz!
#
# /help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!""")
#
#
# @dp.message_handler(commands='help')
# async def start_def(msg: types.Message):
#     await msg.answer(f"""UzGeeks faollari tomonidan tuzilgan Ustoz-Shogird kanali.
#
# Bu yerda Programmalash bo`yicha
#   #Ustoz,
#   #Shogird,
#   #oquvKursi,
#   #Sherik,
#   #Xodim va
#   #IshJoyi
#  topishingiz mumkin.
#
# E'lon berish: @UstozShogirdBot
#
# Admin @UstozShogirdAdminBot""")
#
#
# @dp.message_handler(text='Sherik kerak')
# async def ariza(msg: types.Message, state: FSMContext):
#     await msg.answer(f"""Sherik topish uchun ariza berish
#
# Hozir sizga birnecha savollar beriladi.
# Har biriga javob bering.
# Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
#
# Ism, familiyangizni kiriting?""")
#     await state.set_state('full_name')
#
#
# @dp.message_handler(state='full_name')
# async def ariza(msg: types.Message, state: FSMContext):
#     full_name = msg.text
#     await state.update_data({
#         'full_name': full_name
#     })
#     await msg.answer(f"""📚 Texnologiya:
#
# Talab qilinadigan texnologiyalarni kiriting?
# Texnologiya nomlarini vergul bilan ajrating. Masalan,
#
# Java, C++, C#""")
#     await state.set_state('texnologiya')
#
#
# @dp.message_handler(state='texnologiya')
# async def ariza(msg: types.Message, state: FSMContext):
#     texnologiya = msg.text
#     await state.update_data({
#         'texnologiya': texnologiya
#     })
#     await msg.answer(f"""📞 Aloqa:
#
# Bog`lanish uchun raqamingizni kiriting?
# Masalan, +998 90 123 45 67""")
#     await state.set_state('aloqa')
#
#
# @dp.message_handler(state='aloqa')
# async def ariza(msg: types.Message, state: FSMContext):
#     aloqa = msg.text
#     await state.update_data({
#         'aloqa': aloqa
#     })
#     await msg.answer(f"""🌐 Hudud:
#
# Qaysi hududdansiz?
# Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
#     await state.set_state('hudud')
#
#
# @dp.message_handler(state='hudud')
# async def ariza(msg: types.Message, state: FSMContext):
#     hudud = msg.text
#     await state.update_data({
#         'hudud': hudud
#     })
#     await msg.answer(f"""💰 Narxi:
#
# Tolov qilasizmi yoki Tekinmi?
# Kerak bo`lsa, Summani kiriting?""")
#     await state.set_state('narx')
#
#
# @dp.message_handler(state='narx')
# async def ariza(msg: types.Message, state: FSMContext):
#     narx = msg.text
#     await state.update_data({
#         'narx': narx
#     })
#     await msg.answer(f"""👨🏻‍💻 Kasbi:
#
# Ishlaysizmi yoki o`qiysizmi?
# Masalan, Talaba""")
#     await state.set_state('work')
#
#
# @dp.message_handler(state='work')
# async def ariza(msg: types.Message, state: FSMContext):
#     work = msg.text
#     await state.update_data({
#         'work': work
#     })
#     await msg.answer(f"""🕰 Murojaat qilish vaqti:
#
# Qaysi vaqtda murojaat qilish mumkin?
# Masalan, 9:00 - 18:00""")
#     await state.set_state('vaqti')
#
#
# @dp.message_handler(state='vaqti')
# async def ariza(msg: types.Message, state: FSMContext):
#     vaqti = msg.text
#     await state.update_data({
#         'vaqti': vaqti
#     })
#     await msg.answer(f"""🔎 Maqsad:
#
# Maqsadingizni qisqacha yozib bering.""")
#     await state.set_state('maqsad')
#
# @dp.message_handler(state='maqsad')
# async def ariza(msg: types.Message, state: FSMContext):
#     maqsad = msg.text
#     await state.update_data({
#         'maqsad': maqsad
#     })
#     user = await state.get_data()
#
#     skills = user['texnologiya'].split()
#     for i in skills:
#         if i == "c++" or i == 'C++':
#             print(i)
#     natija = [f"#{item}" for item in skills]
#     a = ' '.join(natija)
#     await msg.answer(f"""Sherik kerak:
#
# 🏅 Sherik: {user['full_name']}
# 📚 Texnologiya: {user['texnologiya']}
# 🇺🇿 Telegram: @{msg.from_user.username}w
# 📞 Aloqa: {user['aloqa']}
# 🌐 Hudud: {user['hudud']}
# 💰 Narxi: {user['narx']}
# 👨🏻‍💻 Kasbi: {user['work']}
# 🕰 Murojaat qilish vaqti: {user['vaqti']}
# 🔎 Maqsad: {user['maqsad']}
#
# #sherik {a} """)


# @dp.message_handler(text='Anketa')
# async def handle_anketa(msg: types.Message, state: FSMContext):
#     await msg.reply('Ismingizni kiriting ? ')
#     await state.set_state('firstName')
#
#
# @dp.message_handler(state='firstName')
# async def handle_anketa(msg: types.Message, state: FSMContext):
#     text = msg.text
#     await state.update_data({
#         'firstName': text
#     })
#     await msg.reply('Familiyangizni kiriting ? ')
#     await state.set_state('lastName')
#
#
# @dp.message_handler(state='lastName')
# async def handle_anketa(msg: types.Message, state: FSMContext):
#     text = msg.text
#     await state.update_data({
#         'lastName': text
#     })
#     await msg.reply('Yoshingizni kiriting ? ')
#     await state.set_state('age')
#
#
# @dp.message_handler(state='age')
# async def handle_anketa(msg: types.Message, state: FSMContext):
#     try:
#         text = int(msg.text)
#     except:
#         await msg.reply("Faqat son kiriting")
#     else:
#         await state.update_data({
#             'age': text
#         })
#         d = await state.get_data()
#         firstName = d.get('firstName')
#         lastName = d.get('lastName')
#         age = d.get('age')
#         await msg.answer('Katta rahmat!')
#         await msg.answer(f"""
#             ism: {firstName}
#             familiya: {lastName}
#             yoshi: {age}
#         """)
#         await state.finish()                                 #so'rovni yakunlash


# @dp.message_handler(content_types=types.ContentType.STICKER)
# async def send_sticker(msg: types.Message):
#     await msg.answer_sticker(msg.sticker.file_id)


# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def send_sticker(msg: types.Message):
#     await msg.answer_photo(photo=msg['photo'][0]['file_id'],
#                            caption=f"@{msg.from_user.username} Ajoyib rasm yubordingiz")
#
#
# @dp.message_handler(text=['Contact', 'contact'])
# async def get_contact(msg: types.Message):
#     # contact = msg
#     # print(contact)
#     await msg.answer_contact('+998990145867', 'Dilshod', 'Murtazoyev')

#
# @dp.message_handler(text="Wepro haqida")
# async def send_message(msg: types.Message):
#     await msg.answer('По каким-то причинам не можете работать или делать домашнее задание дома? '
#                      '- огромная коворкинг зона к вашему распоряжению. Вы можете прийти в Wepro, '
#                      'разместиться за удобным столом, заварить себе кофе и заниматься тем что '
#                      'вам интересно. Мы предоставляем все необходимое, чтобы вы расли и '
#                      'развивались вместе с Wepro. Коворкинг для студентов - абсолютно бесплатный!Ï')
#
#
# @dp.message_handler(text="Kurslar")
# async def language_dars(msg: types.Message):
#     await msg.answer('Kurslarni tanlang', reply_markup=kurslar)
#
#
# @dp.message_handler(text="<<Ortga")
# async def language_dars(msg: types.Message):
#     await msg.delete()
#     await msg.answer('Ortga qaytdi.', reply_markup=startBtn)
#
#
# @dp.message_handler(text="Contacts")
# async def language_dars(msg: types.Message):
#     await msg.answer('Contacts', reply_markup=Contact)
#
#
# @dp.message_handler(content_types=types.ContentType.CONTACT)
# async def language_dars(msg: types.Message):
#     print(msg.contact)
#     await msg.reply('Contact uchun katta rahmat !')
#     await bot.send_contact(chat_id=949677905, phone_number=msg.contact['phone_number'], first_name=msg.contact['first_name'])
#
#
# @dp.message_handler(content_types=types.ContentType.LOCATION)
# async def language_dars(msg: types.Message):
#     location = msg.location
#     await msg.reply('Contact uchun katta rahmat !')
#     # await bot.send_location(chat_id=949677905, )
#     await bot.send_location(chat_id=949677905,longitude=location['longitude'], latitude=location['latitude'])


# @dp.message_handler()