from aiogram import types

from tg_bot.filters import CommandSetParams
from tg_bot.loader import dp


@dp.message_handler(CommandSetParams(), chat_type='private', role_filter='admin')
async def set_params_handler(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
