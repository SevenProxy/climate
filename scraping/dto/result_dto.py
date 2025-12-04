from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class ResultApiOpenMeteo:
    time_r: datetime
    temperature: int
    humidity: float
    wind_speed: int


