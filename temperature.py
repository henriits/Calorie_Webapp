import requests
from selectorlib import Extractor


class Temperature:
    """Represents a value extracted from the timedate.com/weather webpage"""

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def get(self):
        r = requests.get(f"https://www.timeanddate.com/weather/{self.country}/{self.city}")
        c = r.text

        extractor = Extractor.from_yaml_file("temperature.yaml")

        raw_result = extractor.extract(c)
        clean_result = raw_result["temp"].replace("\xa0°C", "")
        return clean_result


if __name__ == "__main__":
    temperature = Temperature(city="tallinn", country="estonia").get()
    print(temperature)
