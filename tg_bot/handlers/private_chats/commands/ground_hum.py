from aiogram import types

from graph_creator import GraphCreator
from tg_bot.filters.commands import CommandGroundHum
from tg_bot.loader import dp
from tg_bot.utils.db_api import GroundValues


@dp.message_handler(CommandGroundHum(), chat_type='private')
async def ground_sensors_request(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    sensor_values = list()
    for sensor_value in GroundValues.select().order_by(GroundValues.id.desc()).limit(10):
        sensor_values.append({
            'timestamp': sensor_value.timestamp,
            'sensor1': sensor_value.sensor1.humidity,
            'sensor2': sensor_value.sensor2.humidity,
            'sensor3': sensor_value.sensor3.humidity,
            'sensor4': sensor_value.sensor4.humidity,
            'sensor5': sensor_value.sensor5.humidity,
            'sensor6': sensor_value.sensor6.humidity
        })
    text = list()
    for i in range(0, len(sensor_values)):
        text.append(
            f"<b>{sensor_values[i].get('timestamp').split('.')[0]}:   </b>{round((sensor_values[i].get('sensor1') + sensor_values[i].get('sensor2') + sensor_values[i].get('sensor3') + sensor_values[i].get('sensor4') + sensor_values[i].get('sensor5') + sensor_values[i].get('sensor6')) / 6, 2)}")
    await message.answer(text='\n'.join(
        [
            'Последние 10 средних показаний с датчиков влажности почвы:',
            *text
        ]
    ))
    data_x = [sensor_value.get('timestamp').split(' ')[1].split('.')[0] for sensor_value in sensor_values]
    data_y = [round((sensor_value.get('sensor1') + sensor_value.get('sensor2') + sensor_value.get(
        'sensor3') + sensor_value.get('sensor4') + sensor_value.get('sensor5') + sensor_value.get('sensor6')) / 6, 2)
              for sensor_value in sensor_values]
    data_y.reverse()
    data_x.reverse()
    graph_creator = GraphCreator()
    graph_creator.create_graph(
        data_x=data_x,
        data_y=data_y,
        output_filename='ground_hum.png'
    )
    await message.answer_photo(photo=open('ground_hum.png', "rb"))
