from abc import ABC, abstractmethod
from typing import Union
from pika.channel import Channel
from app_error import AppError

class MessageBrokerTrait(ABC):

    @abstractmethod
    def connect(self, url: str) -> Union[Channel, AppError]:
        pass

