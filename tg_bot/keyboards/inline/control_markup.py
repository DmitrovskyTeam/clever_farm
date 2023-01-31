from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

control_device = CallbackData('control', 'device', 'action')

control_markup = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Система увлажнения воздуха',
                             callback_data=control_device.new(
                                 device='air_hum_system',
                                 action='no_action'
                             ))
    ],
    [
        InlineKeyboardButton(text='Форточки',
                             callback_data=control_device.new(
                                 device='forks',
                                 action='no_action'
                             ))
    ],
    [
        InlineKeyboardButton(text='⬇️ Системы полива ⬇️',
                             callback_data=control_device.new(
                                 device='waterflows',
                                 action='no_action'
                             ))
    ],
    [
        InlineKeyboardButton(text='1',
                             callback_data=control_device.new(
                                 device='water1',
                                 action='no_action'
                             )),
        InlineKeyboardButton(text='2',
                             callback_data=control_device.new(
                                 device='water2',
                                 action='no_action'
                             )),
        InlineKeyboardButton(text='3',
                             callback_data=control_device.new(
                                 device='water3',
                                 action='no_action'
                             )),
    ],
    [
        InlineKeyboardButton(text='4',
                             callback_data=control_device.new(
                                 device='water4',
                                 action='no_action'
                             )),
        InlineKeyboardButton(text='5',
                             callback_data=control_device.new(
                                 device='water5',
                                 action='no_action'
                             )),
        InlineKeyboardButton(text='6',
                             callback_data=control_device.new(
                                 device='water6',
                                 action='no_action'
                             )),
    ],
])


def get_action_markup(device: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Открыть' if device == 'forks' else 'Включить',
                    callback_data=control_device.new(
                        device=device,
                        action='on'
                    )
                )
            ],
            [
                InlineKeyboardButton(
                    text='Закрыть' if device == 'forks' else 'Выключить',
                    callback_data=control_device.new(
                        device=device,
                        action='off'
                    )
                )
            ]
        ]
    )
