from typing import Union
from interface import MessageBrokerTrait
from app_error import AppError
from dto import PropsRabbit
from pika.channel import Channel

import pika
import json

class RabbitMq(MessageBrokerTrait):
    conn_established: PropsRabbit

    def connect(self, url: str) -> Union[Channel, AppError]:
        try:
            params = pika.URLParameters(url)
            conn = pika.BlockingConnection(params)

            channel = conn.channel()
            channel.queue_declare(queue="climate_channel", durable=True)

            self.conn_established = PropsRabbit(
                connection_r=conn,
                channel=channel
            )
            return channel
        except:
            return AppError.CONNECTION_FALIED

    def send(self, payload) -> Union[None, AppError]:
        try:
            channel = self.conn_established.channel
            channel.basic_publish(
                exchange="",
                routing_key="climate_channel",
                body=json.dumps(payload)
            )
            return
        except:
            return AppError.CHANNEL_ERROR
