from doublex import Spy, ANY_ARG
from doublex_expects import have_been_called_with, any_arg
from expects import expect, equal
from mamba import describe, context, it

from src.use_case.create_highlighted_place_use_case import CreateHighlightedPlace
from src.business.model.highlighted_place import HighlightedPlace
from src.infrastructure.repository.highlighted_place_postgresql_repository import HighlightedPlacePostgresqlRepository

with describe("CreateHighlightedPlace use case"):
    with context("when creating a new highlighted place"):
        with it("should create a new highlighted place with the given name, description, and coordinates"):
            highlighted_place = HighlightedPlace(name="ANY_NAME", description="ANY_DESCRIPTION", coordinates="0,0")
            with Spy(HighlightedPlacePostgresqlRepository) as repository_spy:
                repository_spy.save(ANY_ARG).returns(highlighted_place)
            use_case = CreateHighlightedPlace(repository_spy)

            result = use_case.execute(
                name=highlighted_place.name,
                description=highlighted_place.description,
                coordinates=highlighted_place.coordinates
            )

            expect(result).to(equal(highlighted_place))
            expect(repository_spy.save).to(have_been_called_with(any_arg))
