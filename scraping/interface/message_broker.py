from abc import ABC, abstractmethod
from typing import Union, Self
from app_error import AppError
from dto import ResultApiOpenMeteo

class MessageBrokerTrait(ABC):

    @abstractmethod
    def connect(self, url: str) -> Union[Self, AppError]:
        pass

    @abstractmethod
    def send(self, payload: ResultApiOpenMeteo) -> Union[None, AppError]:
        pass

