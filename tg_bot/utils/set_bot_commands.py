from aiogram import types, Dispatcher
from aiogram.types import BotCommandScopeChat

from data.config import ADMINS


async def set_commands(dp: Dispatcher, chat_id: str):
    await dp.bot.set_my_commands(
        commands=
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
        ] if chat_id in ADMINS else
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
        ],
        scope=BotCommandScopeChat(
            chat_id=chat_id
        )

    )
