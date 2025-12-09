from dataclasses import dataclass
from typing import Union
from datetime import datetime
from aiohttp import ClientSession

from dto import ResultApiOpenMeteo
from interface import ApiTrait
from app_error import AppError

from .entity import Api

class OpenWeatherMap(ApiTrait):
    entity: Api
    response_code: int

    def __init__(self, entity: Api) -> None:
        self.entity = entity
        self.response_code = [200, 201, 2003]

    async def get_response_api(self, session: ClientSession) -> Union[ResultApiOpenMeteo, AppError]:
        try:
            async with session.get(self.entity.url) as response:
                response.raise_for_status()
                result = await response.json()

                time = datetime.now()
                current = result["current"]
                hourly = result["hourly"]

                return ResultApiOpenMeteo(
                    time_r=time,
                    temperature=current["temperature_2m"],
                    humidity=hourly["relative_humidity_2m"],
                    wind_speed=current["wind_speed_10m"]
                )
        except:
            return AppError.INVALID_STATUS


