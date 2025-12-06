from dataclasses import dataclass
from pika import BlockingConnection, Channel
from pika.channel import Channel
from pika.BlockingConnection import BlockingConnection

@dataclass
class PropsRabbit:
    connection_r: BlockingConnection
    channel: Channel
