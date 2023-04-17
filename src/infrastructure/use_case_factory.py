import os

from src.use_case.create_highlighted_place_use_case import CreateHighlightedPlace
from src.use_case.delete_highlighted_place_use_case import DeleteHighlightedPlace
from src.use_case.get_all_highlighted_places_use_case import GetAllHighlightedPlaces
from src.use_case.get_highlighted_place_use_case import GetHighlightedPlace
from src.infrastructure.repository.highlighted_place_postgresql_repository import HighlightedPlacePostgresqlRepository
from src.infrastructure.services.forecast_retriever import ForecastRetriever

CONNECTION_STRING = os.environ.get('DATABASE_CONNECTION_STRING')


def _highlighted_place_postgresql_repository():
    return HighlightedPlacePostgresqlRepository(conn_string=CONNECTION_STRING)


def _forecast_retriever():
    return ForecastRetriever()


def get_highlighted_place_use_case():
    return GetHighlightedPlace(_highlighted_place_postgresql_repository(), _forecast_retriever())


def get_all_highlighted_places_use_case():
    return GetAllHighlightedPlaces(_highlighted_place_postgresql_repository(), _forecast_retriever())


def create_highlighted_place_use_case():
    return CreateHighlightedPlace(_highlighted_place_postgresql_repository())


def delete_highlighted_place_use_case():
    return DeleteHighlightedPlace(_highlighted_place_postgresql_repository())
