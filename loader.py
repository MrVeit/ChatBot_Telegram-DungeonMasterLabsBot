import asyncio

from bot_items.config import bot_token
from aiogram import types, Bot, executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()
loop = asyncio.get_event_loop()
bot = Bot(token=bot_token, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot, loop=loop)
