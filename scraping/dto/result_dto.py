from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime

@dataclass
class ResultApiOpenMeteo:
    time_r: datetime
    temperature: float
    humidity: List
    wind_speed: float


