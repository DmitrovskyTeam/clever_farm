from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from data import BOT_TOKEN, REDIS_HOST, REDIS_PORT, REDIS_PASS

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = RedisStorage2(host=REDIS_HOST,
                        port=REDIS_PORT,
                        password=REDIS_PASS)
# storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
