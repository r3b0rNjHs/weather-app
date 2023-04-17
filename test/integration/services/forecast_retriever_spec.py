from expects import expect, be_an
from mamba import describe, it

from src.infrastructure.services.forecast_retriever import ForecastRetriever

with describe("Forecast Retriever should"):
    with it("return a valid forecast for today and tomorrow with the temperature, humidity and precipitation"):
        # Coordinates for Güigüi beach in Gran Canaria
        coordinates = '27.9486,15.8279'
        forecast = ForecastRetriever().get_forecast(coordinates)

        expect(forecast.today.temperature).to(be_an(float))
        expect(forecast.today.humidity).to(be_an(float))
        expect(forecast.today.precipitation).to(be_an(float))
        expect(forecast.tomorrow.temperature).to(be_an(float))
        expect(forecast.tomorrow.humidity).to(be_an(float))
        expect(forecast.tomorrow.precipitation).to(be_an(float))
