from dataclasses import dataclass
from typing import Union
from datetime import datetime

from dto import ResultApiOpenMeteo
from interface import ApiTrait
from app_error import AppError

from .entity import Api

import requests


class OpenWeatherMap(ApiTrait):
    entity: Api
    response_code: int

    def __init__(self, entity: Api) -> None:
        self.entity = entity
        self.response_code = [200, 201, 2003]

    def get_response_api(self) -> Union[ResultApiOpenMeteo, AppError]:
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0",
            "Host": "api.open-meteo.com"
        }
        try:
            response = requests.get(self.entity.url, headers=headers)
            response.raise_for_status()
            if response.status_code not in self.response_code:
                return AppError.INVALID_URL

            result = response.json()

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


