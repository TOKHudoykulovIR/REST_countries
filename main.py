import logging
import os

from aiogram import Bot, Dispatcher, executor
from handlers import register_commands
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand
from dotenv import load_dotenv

load_dotenv()


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/menu", description="Open menu"),
    ]
    await bot.set_my_commands(commands)

storage = MemoryStorage()

API_TOKEN = os.environ.get('api_key')
print(API_TOKEN)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

register_commands(dp)


async def on_startup(dp):
    await set_commands(bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
