from aiogram import executor

from tg_bot.loader import dp
# import middlewares, filters,
from tg_bot import filters, handlers
from tg_bot.utils.notify_admins import on_startup_notify, on_shutdown_notify


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)


async def on_shutdown(dispatcher):
    await on_shutdown_notify(dispatcher)


executor.start_polling(dispatcher=dp,
                       on_startup=on_startup,
                       on_shutdown=on_shutdown)
