"""
AUTO_BOT weather API

Developers: Andrey Kozlovsky, Stanislav Ermokhin

"""

import requests
import json

from config import WEATHER_API


class OpenWeatherForecast:

    _city_cache = dict()

    @classmethod
    def get(cls, city):
        """A fine method"""

        # if city.lower() not in cls._city_cache:

        try:

            url = f'http://api.openweathermap.org/data/2.5/weather?q={city.lower()}'\
                  f'&appid={WEATHER_API}&mode=json&units=metric'

            weather = requests.get(url).text

            cls._city_cache[city.lower()] = json.loads(weather)

            return json.loads(weather)

        except Exception as error:
            return error

        # else:
            # return cls._city_cache[city.lower()]


class CityInfo(object):
    """A fine class"""

    def __init__(self, city=None, weather_forecast=None):
        """A fine initializer"""

        self.city = city or 'Novosibirsk'
        self._weather_forecast = weather_forecast or OpenWeatherForecast()
        self.description_bad = {'rain', 'snow',
                                'heavy', 'tornado',
                                'mist', 'haze',
                                'sand', 'smoke',
                                'fog', 'dust',
                                'volcanic', 'squall',
                                'sleet'}

    def weather_forecast(self):
        """A fine method"""

        return self._weather_forecast.get(self.city)

    def write(self):
        """A fine method"""

        with open('log.txt', 'a') as a:
            a.write(str(self._weather_forecast.get(self.city)) + '\n')

        return self.weather_forecast()

