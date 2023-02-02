from aiogram import types
from aiogram.types import CallbackQuery

from db_api import TempHumValues
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
    if device == 'forks':
        last_sensors_value = TempHumValues.select().order_by(TempHumValues.id.desc()).limit(1)[0]
        cur_temp = (
                               last_sensors_value.sensor1.temperature + last_sensors_value.sensor2.temperature + last_sensors_value.sensor3.temperature + last_sensors_value.sensor4.temperature) / 4
        if cur_temp < 25:
            message_text = '\n\n<b>Температура воздуха ниже 25°. Возможность открытия форточек сейчас заблокирована</b>'
            param = 'close'

        elif cur_temp > 34:
            message_text = '\n\n<b>Температура воздуха выше 34°. Возможность закрытия форточек сейчас заблокирована</b>'
            param = 'open'
        else:
            message_text = ''
            param = 'all'
    elif device == 'air_hum_system':
        last_sensors_value = TempHumValues.select().order_by(TempHumValues.id.desc()).limit(1)[0]
        cur_hum = (
                              last_sensors_value.sensor1.humidity + last_sensors_value.sensor2.humidity + last_sensors_value.sensor3.humidity + last_sensors_value.sensor4.humidity) / 4
        if cur_hum < 40:
            message_text = '\n\n<b>Влажность воздуха ниже 25°. Возможность выключения системы увлажнения сейчас заблокирована</b>'
            param = 'close'
        elif cur_hum > 80:
            message_text = '\n\n<b>Влажность воздуха выше 34°. Возможность включения системы увлажнения сейчас заблокирована</b>'
            param = 'open'
        else:
            message_text = ''
            param = 'all'
    await dp.bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text='Выберите действие' + message_text,
        reply_markup=get_action_markup(device, param)
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
