from aiogram import types

from tg_bot.filters.commands import CommandAirHum
from tg_bot.loader import dp
from tg_bot.utils.db_api import TempHumValues


@dp.message_handler(CommandAirHum(), chat_type='private')
async def air_temp_request(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    sensor_values = list()
    for sensor_value in TempHumValues.select().order_by(TempHumValues.id.desc()).limit(10):
        sensor_values.append({
            'timestamp': sensor_value.timestamp,
            'sensor1': sensor_value.sensor1.humidity,
            'sensor2': sensor_value.sensor2.humidity,
            'sensor3': sensor_value.sensor3.humidity,
            'sensor4': sensor_value.sensor4.humidity
        })
    text = list()
    for i in range(0, len(sensor_values)):
        text.append(
            f"<b>{sensor_values[i].get('timestamp').split('.')[0]}:   </b>{(sensor_values[i].get('sensor1') + sensor_values[i].get('sensor2') + sensor_values[i].get('sensor3') + sensor_values[i].get('sensor4')) / 4}")
    await message.answer(text='\n'.join(
        [
            'Последние 10 средних показаний с датчика влажности воздуха:',
            *text
        ]
    ))
