from aiogram import executor

from tg_bot.loader import dp
# import middlewares, filters,
from tg_bot import filters, handlers
from tg_bot.utils import on_startup_notify, on_shutdown_notify, on_startup_sqlite, on_shutdown_sqlite, run_blocking_io


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)
    await run_blocking_io(on_startup_sqlite)


async def on_shutdown(dispatcher):
    await on_shutdown_notify(dispatcher)
    await run_blocking_io(on_shutdown_sqlite)


executor.start_polling(dispatcher=dp,
                       on_startup=on_startup,
                       on_shutdown=on_shutdown)
