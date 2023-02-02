from aiogram import types
from aiogram.types import CallbackQuery

from farm_api_module import FarmApiModule
from tg_bot.filters.commands import CommandControl
from tg_bot.keyboards.inline import control_markup, control_device, get_action_markup
from tg_bot.loader import dp


@dp.message_handler(CommandControl(), chat_type='private', role_filter='admin')
async def control_command_with_admin(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    await message.answer(text='Выберите, чем хотите управлять',
                         reply_markup=control_markup)


@dp.callback_query_handler(
    control_device.filter(
        device='waterflows',
        action='no_action'
    ),
    chat_type='private',
    role_filter='admin'
)
async def no_action_waterflows(call: CallbackQuery):
    await call.answer(cache_time=1)


@dp.callback_query_handler(
    control_device.filter(
        action='no_action'
    ),
    chat_type='private',
    role_filter='admin'
)
async def no_waterflow_system(call: types.CallbackQuery, callback_data: dict):
    device = callback_data.get('device')
    await dp.bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text='Выберите действие',
        reply_markup=get_action_markup(device)
    )


@dp.callback_query_handler(
    control_device.filter(),
    chat_type='private',
    role_filter='admin'
)
async def make_action(call: CallbackQuery, callback_data: dict):
    if callback_data.get('device') == 'waterflows':
        await call.answer(cache_time=1)
        return
    action_arg = 1 if callback_data.get('action') == 'on' else 0
    farm_api = FarmApiModule()
    if callback_data.get('device') == 'forks':
        farm_api.control_windows(state=action_arg)
        await dp.bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"Команда на {'открытие' if action_arg == 1 else 'закрытие'} окон отправлена",
            reply_markup=None
        )
    else:
        if callback_data.get('device') == 'air_hum_system':
            farm_api.control_humidity_system(state=action_arg)
            await dp.bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=f"Команда на {'включение' if action_arg == 1 else 'выключение'} системы увлажнения воздуха отправлена",
                reply_markup=None
            )
        if callback_data.get('device')[:-1] == 'water':
            farm_api.control_watering(pomp_id=int(callback_data.get('device')[-1]), state=action_arg)
            await dp.bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=f"Команда на {'включение' if action_arg == 1 else 'выключение'} системы полива {int(callback_data.get('device')[-1])} борозды на грядке отправлена",
                reply_markup=None
            )


@dp.message_handler(CommandControl(), chat_type='private')
async def control_command_no_admin(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    await message.answer(text='Команда /control доступна только администраторам')
