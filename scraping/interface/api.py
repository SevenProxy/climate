from abc import ABC, abstractmethod
from typing import Union
from .api import AppError
from dto import ResultApiOpenMeteo

class ApiTrait:

    @abstractmethod
    def get_response_api(self) -> Union[ResultApiOpenMeteo, AppError]:
        pass

