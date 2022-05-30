from aiogram.types import ReplyKeyboardRemove

from keyboards import menu_keyboard, regions_keyboard
from get_data import random_country, regions, country_search
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMRegion(StatesGroup):
    state1 = State()
    state2 = State()
    state3 = State()


async def menu(message: types.Message):
    await FSMRegion.state1.set()
    await message.answer("Choose category ↘︎", reply_markup=menu_keyboard)


async def all_countries_btn(message: types.Message, state: FSMContext):
    if message.text == 'Random country 🌍':
        await message.answer('▷▷▷', reply_markup=ReplyKeyboardRemove())
        await random_country(message)
        await state.finish()
    elif message.text == 'Random countries by regions 🗺':
        await message.answer("Choose region...", reply_markup=regions_keyboard)
        await FSMRegion.next()
    elif message.text == "Search specific country 🔎":
        await message.answer("Enter country name...", reply_markup=ReplyKeyboardRemove())
        await FSMRegion.state3.set()


async def countries_by_regions_btn(message: types.Message, state: FSMContext):
    if message.text == "Back ⬅️":
        await message.answer("▷▷▷", reply_markup=menu_keyboard)
        await FSMRegion.state1.set()
    else:
        await regions(message.text, message)
        await state.finish()


async def specific_country_btn(message: types.Message, state: FSMContext):
    await country_search(message, message.text)
    await state.finish()


def register_commands(dp: Dispatcher):
    dp.register_message_handler(menu, commands="menu", state="*")
    dp.register_message_handler(all_countries_btn, state=FSMRegion.state1)
    dp.register_message_handler(countries_by_regions_btn, state=FSMRegion.state2)
    dp.register_message_handler(specific_country_btn, state=FSMRegion.state3)
