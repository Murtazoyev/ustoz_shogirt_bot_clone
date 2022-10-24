from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Sherik kerak'),
            KeyboardButton(text='Ish joyi kerak'),
        ], [
            KeyboardButton(text='Hodim Kerak'),
            KeyboardButton(text='Ustoz kerak'),
        ], [
           KeyboardButton(text='Shogirt kerak')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

adminga_yuborish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q"),
        ]
    ],
    resize_keyboard=True,
)


Contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Contact', request_contact=True),
            KeyboardButton(text='Location', request_location=True),
        ],
        [
            KeyboardButton(text="<<Ortga")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)