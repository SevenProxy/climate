from dataclasses import dataclass
from pika.channel import Channel
from pika import BlockingConnection

@dataclass
class PropsRabbit:
    connection_r: BlockingConnection
    channel: Channel
