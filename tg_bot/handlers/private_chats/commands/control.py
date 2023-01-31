from aiogram import types

from tg_bot.filters.commands import CommandControl
from tg_bot.loader import dp


@dp.message_handler(CommandControl(), chat_type='private')
async def air_temp_request(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    await message.answer(text='Команда /control доступна только администраторам')
