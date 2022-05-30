from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Random country 🌍"),
        ],
        [
            KeyboardButton(text="Random countries by regions 🗺"),
        ],
        [
            KeyboardButton(text="Search specific country 🔎"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
)

regions_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Africa"),
            KeyboardButton(text="Americas"),
            KeyboardButton(text="Asia"),
        ],
        [
            KeyboardButton(text="Europe"),
            KeyboardButton(text="Oceania"),
        ],
        [
            KeyboardButton(text="Back ⬅️"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
)
