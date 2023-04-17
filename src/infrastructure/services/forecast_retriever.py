import requests

from src.business.services.forecast_retriever import IForecastRetriever
from src.business.model.forecast import ForecastDetails, Forecast

# TODO: Move to a config file
API_KEY = '5f3a7e05d9de4358bda111000231604'


class ForecastRetriever(IForecastRetriever):
    def get_forecast(self, coordinates):
        url = f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={coordinates}&days=2&aqi=no&alerts=no"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        details = []
        for daily in data["forecast"]["forecastday"][:2]:
            temperature = daily["day"]["avgtemp_c"]
            humidity = daily["day"]["avghumidity"]
            precipitation = daily["day"]["totalprecip_mm"]
            details.append(ForecastDetails(temperature, humidity, precipitation))

        return Forecast(details[0], details[1])
