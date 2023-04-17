from doublex import Spy, Stub, ANY_ARG
from doublex_expects import have_been_called_with
from expects import expect, contain
from mamba import it, describe

from src.use_case.get_all_highlighted_places_use_case import GetAllHighlightedPlaces
from src.business.services.forecast_retriever import IForecastRetriever
from src.business.model.forecast import Forecast, ForecastDetails
from src.business.model.highlighted_place import HighlightedPlace
from src.infrastructure.repository.highlighted_place_postgresql_repository import HighlightedPlacePostgresqlRepository

with describe("GetAllHighlightedPlaces") as self:
    with it("should return all the highlighted places stored in the repository"):
        any_highlighted_place = HighlightedPlace(name="AnyName", description="Any description", coordinates="1,1")
        another_highlighted_place = HighlightedPlace(name="AnotherName", description="Another description", coordinates="2,2")
        with Spy(HighlightedPlacePostgresqlRepository) as repository:
            repository.get_all().returns([any_highlighted_place, another_highlighted_place])

        with Stub(IForecastRetriever) as forecast_retriever:
            forecast_retriever.get_forecast(ANY_ARG).returns(Forecast(
                today=ForecastDetails(
                    temperature=20.5,
                    humidity=60.3,
                    precipitation=0.4,
                ),
                tomorrow=ForecastDetails(
                    temperature=20.5,
                    humidity=60.3,
                    precipitation=0.4,
                )
            ))

        use_case = GetAllHighlightedPlaces(repository, forecast_retriever)
        result = use_case.execute()

        expect(repository.get_all).to(have_been_called_with())
        expect(result).to(contain(any_highlighted_place))
        expect(result).to(contain(another_highlighted_place))
