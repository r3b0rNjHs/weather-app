from src.business.model.highlighted_place import HighlightedPlace
from src.business.services.forecast_retriever import IForecastRetriever
from src.business.services.highlighted_place_repository import HighlightedPlaceRepository


class GetHighlightedPlace:
    def __init__(self, repository: HighlightedPlaceRepository, forecast_retriever: IForecastRetriever):
        self.repository = repository
        self.forecast_retriever = forecast_retriever

    def execute(self, highlighted_place_id) -> HighlightedPlace:
        highlighted_place = self.repository.retrieve_by_id(highlighted_place_id)
        highlighted_place.forecast = self.forecast_retriever.get_forecast(highlighted_place.coordinates)
        return highlighted_place
