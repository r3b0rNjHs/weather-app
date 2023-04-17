from doublex import Spy, Stub, ANY_ARG
from doublex_expects import have_been_called_with
from expects import expect, equal
from mamba import describe, context, it

from src.use_case.get_highlighted_place_use_case import GetHighlightedPlace
from src.business.services.forecast_retriever import IForecastRetriever
from src.business.services.highlighted_place_repository import HighlightedPlaceRepository
from src.business.model.forecast import Forecast, ForecastDetails
from src.business.model.highlighted_place import HighlightedPlace

with describe("GetHighlightedPlace use case"):
    with context("when getting an existing highlighted place"):
        with it("should return the highlighted place with the given ID"):
            highlighted_place = HighlightedPlace(
                id=1,
                name="ANY_NAME",
                description="ANY_DESCRIPTION",
                coordinates="1,1"
            )

            with Spy(HighlightedPlaceRepository) as repository:
                repository.retrieve_by_id(highlighted_place.id).returns(highlighted_place)

            with Stub(IForecastRetriever) as forecast_retriever:
                forecast_retriever.get_forecast(highlighted_place.coordinates).returns(Forecast(
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

            use_case = GetHighlightedPlace(repository, forecast_retriever)

            result = use_case.execute(1)
            expect(result).to(equal(highlighted_place))

            expect(repository.retrieve_by_id).to(have_been_called_with(1))
