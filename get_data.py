import random
import requests
from aiogram.types import ReplyKeyboardRemove


async def random_country(message):
    n = random.randint(0, 249)
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    data = response.json()
    await get_country_info(n, data, message)


async def countries_by_region(message, region, country_qty):
    await message.answer("▷▷▷", reply_markup=ReplyKeyboardRemove())
    n = random.randint(0, country_qty)
    url = f"https://restcountries.com/v3.1/region/{region}"
    response = requests.get(url)
    data = response.json()
    await get_country_info(n, data, message)


async def regions(region, message):
    if region == "Europe":
        await countries_by_region(message, "europe", 52)
    elif region == "Asia":
        await countries_by_region(message, "asia", 49)
    elif region == "Americas":
        await countries_by_region(message, "americas", 55)
    elif region == "Oceania":
        await countries_by_region(message, "oceania", 26)
    elif region == "Africa":
        await countries_by_region(message, "africa", 58)


async def country_search(message, country):
    url = f"https://restcountries.com/v3.1/name/{country}?fullText=true"
    response = requests.get(url)
    data = response.json()
    await get_country_info(0, data, message)


async def get_country_info(n, data, message):
    name_common = data[n]['name']['common']
    print(name_common)
    name_official = data[n]['name']['official']
    capital = " ".join(data[n]['capital'])
    is_independent = data[n]['independent']
    if is_independent:
        is_independent = "Yes"
    else:
        is_independent = "No"
    languages = None
    for lan in data[n]['languages']:
        languages = data[n]['languages'][lan]
    currencies = None
    for c in data[n]['currencies']:
        currencies = data[n]['currencies'][c]['name']
    top_lvl_domain = " ".join(data[n]['tld'])

    location = data[n]['region']
    try:
        sub_location = data[n]['subregion']
    except (Exception,):
        sub_location = None

    area = "{:,}".format(data[n]['area'])
    flag_emoji = data[n]['flag']
    population = "{:,}".format(data[n]['population'])
    try:
        borders = len(data[n]['borders'])
    except (Exception,):
        borders = None
    start_of_week = data[n]['startOfWeek']

    await message.answer(f'𝙲𝙾𝙼𝙼𝙾𝙽 𝙽𝙰𝙼𝙴 {flag_emoji}   →   {name_common} \n'
                         # f'𝙾𝙵𝙵𝙸𝙲𝙸𝙰𝙻 𝙽𝙰𝙼𝙴 ・・・→   {name_official} \n'
                         f'𝙲𝙰𝙿𝙸𝚃𝙰𝙻 🏛          →   {capital} \n'
                         f'𝙸𝚂 𝙸𝙽𝙳𝙴𝙿𝙴𝙽𝙳𝙴𝙽𝚃 🗽  →   {is_independent} \n'
                         f'𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴𝚂 💬          →   {languages} \n'
                         f'𝙲𝚄𝚁𝚁𝙴𝙽𝙲𝙸𝙴𝚂 💵        →   {currencies} \n'
                         f'𝚃𝙾𝙿 𝙻𝚅𝙻 𝙳𝙾𝙼𝙰𝙸𝙽 🌐  →   {top_lvl_domain} \n'
                         f'𝙻𝙾𝙲𝙰𝚃𝙸𝙾𝙽 🌏             →    {location} \n'
                         f'𝚂𝚄𝙱 𝙻𝙾𝙲𝙰𝚃𝙸𝙾𝙽 🗺     →    {sub_location} \n'
                         f'𝙰𝚁𝙴𝙰 🏝                      →    {area} \n'
                         f'𝙿𝙾𝙿𝚄𝙻𝙰𝚃𝙸𝙾𝙽 👨‍👩‍👧‍👦        →    {population} \n'
                         f'𝙱𝙾𝚁𝙳𝙴𝚁𝚂 🚧               →    {borders}',
                         parse_mode="Markdown"
                         )

    flag = data[n]['flags']['png']
    r = requests.get(flag)
    file = open("flag.png", "wb")
    file.write(r.content)
    file.close()

    await message.answer_photo(photo=open("flag.png", "rb"))
