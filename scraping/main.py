from core import Api, OpenWeatherMap, RabbitMq
from app_error import AppError
from dto import ResultApiOpenMeteo
from dotenv import load_dotenv

import os
import aiohttp
import asyncio

load_dotenv()

SLEEP_TIME = 60 * 60 * 1

async def main() -> None:
    open_weather: Api = Api(url=os.getenv("URL_API"))
    rabbit_connect = RabbitMq()

    usecase: OpenWeatherMap = OpenWeatherMap(entity=open_weather)

    async with aiohttp.ClientSession() as session:
        while True:
            result = await usecase.get_response_api(session)

            match result:
                case ResultApiOpenMeteo():
                    conn = rabbit_connect.connect(os.getenv("RABBIT_LOGIN"))
                    match conn:
                        case AppError.CONNECTION_FALIED:
                            print(conn)
                        case _:
                            send_rabbit = conn.send(result)
                            match send_rabbit:
                                case None:
                                    print("NICE!!!")
                                case _:
                                    print(send_rabbit)
                case _:
                    print(result)


            await asyncio.sleep(SLEEP_TIME)

asyncio.run(main())
