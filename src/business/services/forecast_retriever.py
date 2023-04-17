from abc import abstractmethod


class IForecastRetriever:
    @abstractmethod
    def get_forecast(self, coordinates: str):
        pass
