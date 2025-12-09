from typing import Union, Self
from interface import MessageBrokerTrait
from app_error import AppError
from dto import PropsRabbit, ResultApiOpenMeteo

import pika
import json

class RabbitMq(MessageBrokerTrait):
    conn_established: PropsRabbit

    def connect(self, url: str) -> Union[Self, AppError]:
        try:
            params = pika.URLParameters(url)
            conn = pika.BlockingConnection(params)

            channel = conn.channel()
            channel.queue_declare(queue="climate_channel", durable=True)

            self.conn_established = PropsRabbit(
                connection_r=conn,
                channel=channel
            )
            return self
        except:
            return AppError.CONNECTION_FALIED

    def send(self, payload: ResultApiOpenMeteo) -> Union[None, AppError]:
        try:
            channel = self.conn_established.channel
            channel.basic_publish(
                exchange="",
                routing_key="climate_channel",
                body=json.dumps({
                    "time": payload.time_r.strftime("%d/%m/%Y"),
                    "temperature": payload.temperature,
                    "humidity": payload.humidity,
                    "wind_speed": payload.wind_speed,
                })
            )
            return
        except:
            return AppError.CHANNEL_ERROR
