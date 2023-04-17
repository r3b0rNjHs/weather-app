from doublex import Spy
from doublex_expects import have_been_called_with
from expects import expect, equal
from mamba import describe, context, it

from app import HighlightedPlace
from src.use_case.delete_highlighted_place_use_case import DeleteHighlightedPlace
from src.infrastructure.repository.highlighted_place_postgresql_repository import HighlightedPlacePostgresqlRepository

with describe("DeleteHighlightedPlace use case"):
    with context("when deleting an existing highlighted place"):
        with it("should delete the highlighted place with the given ID and return it"):
            highlighted_place = HighlightedPlace(id=1, name="ANY_NAME", description="ANY_DESCRIPTION", coordinates="1,1")
            with Spy(HighlightedPlacePostgresqlRepository) as repository:
                repository.retrieve_by_id(1).returns(highlighted_place)
                repository.remove(highlighted_place).returns(highlighted_place)
            use_case = DeleteHighlightedPlace(repository)

            result = use_case.execute(1)
            expect(result).to(equal(highlighted_place))

            expect(repository.retrieve_by_id).to(have_been_called_with(1))
            expect(repository.remove).to(have_been_called_with(highlighted_place))
