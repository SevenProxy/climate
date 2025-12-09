from abc import ABC, abstractmethod
from typing import Union
from app_error import AppError
from dto import ResultApiOpenMeteo
from aiohttp import ClientSession

class ApiTrait(ABC):

    @abstractmethod
    async def get_response_api(self, session: ClientSession) -> Union[ResultApiOpenMeteo, AppError]:
        pass

