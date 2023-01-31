from .commands import CommandAirTemp, CommandControl, CommandAirHum, CommandGroundHum
from .role_filter import RoleFilter
from ..loader import dp

if __name__ == "filters":
    dp.filters_factory.bind(RoleFilter)

__all__ = [CommandAirTemp, CommandControl, CommandAirHum, CommandGroundHum, RoleFilter]
