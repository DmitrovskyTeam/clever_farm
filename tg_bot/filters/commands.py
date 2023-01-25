from aiogram.dispatcher.filters import Command


class CommandAirTemp(Command):
    def __init__(self):
        super().__init__(['airtemp'])


class CommandAirHum(Command):
    def __init__(self):
        super().__init__(['airhum'])


class CommandGroundHum(Command):
    def __init__(self):
        super().__init__(['groundhum'])


class CommandControl(Command):
    def __init__(self):
        super().__init__(['control'])
