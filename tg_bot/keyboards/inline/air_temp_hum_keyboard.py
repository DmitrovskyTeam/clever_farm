from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

air_tem_him_callback_data = CallbackData('air_hum_callback', 'param', 'action')


def get_air_temp_hum_keyboard(param: str, sensor_list: set):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f'{"✅" if 1 in sensor_list else "❌"} 1 датчик',
                    callback_data=air_tem_him_callback_data.new(
                        param=param,
                        action='rm_1' if 1 in sensor_list else 'add_1'
                    )
                )
            ],
            [
                InlineKeyboardButton(
                    text=f'{"✅" if 2 in sensor_list else "❌"} 2 датчик',
                    callback_data=air_tem_him_callback_data.new(
                        param=param,
                        action='rm_2' if 2 in sensor_list else 'add_2'
                    )
                )
            ],
            [
                InlineKeyboardButton(
                    text=f'{"✅" if 3 in sensor_list else "❌"} 3 датчик',
                    callback_data=air_tem_him_callback_data.new(
                        param=param,
                        action='rm_3' if 3 in sensor_list else 'add_3'
                    )
                )
            ],
            [
                InlineKeyboardButton(
                    text=f'{"✅" if 4 in sensor_list else "❌"} 4 датчик',
                    callback_data=air_tem_him_callback_data.new(
                        param=param,
                        action='rm_4' if 4 in sensor_list else 'add_4'
                    )
                )
            ],
            [
                InlineKeyboardButton(
                    text=f'{"✅" if 5 in sensor_list else "❌"} Среднее значение {"температуры" if param == "temp" else "влажности воздуха"}',
                    callback_data=air_tem_him_callback_data.new(
                        param=param,
                        action='rm_5' if 5 in sensor_list else 'add_5'
                    )
                )
            ],
            [
                InlineKeyboardButton(
                    text='Показать',
                    callback_data=air_tem_him_callback_data.new(
                        param='complete_' + param,
                        action=f'show'
                    )
                )
            ]
        ]
    )
