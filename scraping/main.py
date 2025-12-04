from core import Api, OpenWeatherMap
from dto import ResultApiOpenMeteo
from interface import AppError

def main() -> None:
    open_weather: Api = Api(url="https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")

    usecase: OpenWeatherMap = OpenWeatherMap(entity=open_weather)
    result = usecase.get_response_api()

    print("result:")
    print(result)
    #if isinstance(result, )

main()
