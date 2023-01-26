from aiogram import types

from tg_bot.filters.commands import CommandAirTemp
from tg_bot.loader import dp


@dp.message_handler(CommandAirTemp(), chat_type='private')
async def air_temp_request(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)