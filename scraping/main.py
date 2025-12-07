from core import Api, OpenWeatherMap, RabbitMq
from app_error import AppError
from dto import PropsRabbit, ResultApiOpenMeteo
from dotenv import load_dotenv
from pika.channel import Channel

import os

load_dotenv()

def main() -> None:
    open_weather: Api = Api(url=os.getenv("URL_API"))
    rabbit_connect = RabbitMq()

    usecase: OpenWeatherMap = OpenWeatherMap(entity=open_weather)
    result = usecase.get_response_api()

    match result:
        case ResultApiOpenMeteo():
            conn = rabbit_connect.connect(os.getenv("RABBIT_LOGIN"))
            match conn:
                case Channel():
                    send_rabbit = conn.send(result)
                    match send_rabbit:
                        case None:
                            print("NICE!!!")
                        case _:
                            print(send_rabbit)
                case _:
                    print(conn)
        case _:
            print(result)

main()
