from typing import List

from src.business.services.forecast_retriever import IForecastRetriever
from src.business.services.highlighted_place_repository import HighlightedPlaceRepository
from src.business.model.highlighted_place import HighlightedPlace


class GetAllHighlightedPlaces:
    def __init__(self, repository: HighlightedPlaceRepository, forecast_retriever: IForecastRetriever):
        self.repository = repository
        self.forecast_retriever = forecast_retriever

    def execute(self) -> List[HighlightedPlace]:
        places = self.repository.get_all()
        for place in places:
            place.forecast = self.forecast_retriever.get_forecast(place.coordinates)
        return places
