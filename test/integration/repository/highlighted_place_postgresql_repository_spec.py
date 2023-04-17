import os

import psycopg2
from expects import expect, equal, contain
from mamba import context, it, before, describe

from src.business.model.highlighted_place import HighlightedPlace
from src.infrastructure.repository.highlighted_place_postgresql_repository import HighlightedPlacePostgresqlRepository

with describe("HighlightedPlacePostgresqlRepository") as self:
    with before.each:
        CONNECTION_STRING = os.environ.get('DATABASE_CONNECTION_STRING')
        self.repository = HighlightedPlacePostgresqlRepository(CONNECTION_STRING)

        with psycopg2.connect(CONNECTION_STRING) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM highlighted_places")
            cursor.close()

        self.given_highlighted_place = HighlightedPlace(
            name="ANY_NAME",
            description="ANY_DESCRIPTION",
            coordinates="1234567890,0987654321"
        )


    with context("when adding a new highlighted place"):
        with it("should add the highlighted place to the database and return it with the ID assigned"):
            highlighted_place = self.given_highlighted_place
            result = self.repository.save(highlighted_place)

            expect(result.id).not_to(equal(None))
            expect(result.name).to(equal("ANY_NAME"))
            expect(result.description).to(equal("ANY_DESCRIPTION"))
            expect(result.coordinates).to(equal("1234567890,0987654321"))

    with context("when getting an existing highlighted place"):
        with it("should return the highlighted place with the given ID"):
            highlighted_place = self.given_highlighted_place
            added_highlighted_place = self.repository.save(highlighted_place)

            result = self.repository.retrieve_by_id(added_highlighted_place.id)
            expect(result.name).to(equal(added_highlighted_place.name))

    with context("when deleting an existing highlighted place"):
        with it("should delete the highlighted place with the given ID and return it"):
            highlighted_place = self.given_highlighted_place
            added_highlighted_place = self.repository.save(highlighted_place)

            result = self.repository.remove(added_highlighted_place)
            expect(result).to(equal(added_highlighted_place))

            result = self.repository.retrieve_by_id(added_highlighted_place.id)
            expect(result).to(equal(None))

    with context("when there are no highlighted places stored in the database"):
        with it("should return an empty list"):
            highlighted_places = self.repository.get_all()
            expect(highlighted_places).to(equal([]))

    with context("when there are highlighted places stored in the database"):
        with it("should return all the highlighted places stored in the database"):
            highlighted_place1 = self.given_highlighted_place
            highlighted_place2 = HighlightedPlace(name="AnotherName", description="Another description", coordinates="3,3")

            self.repository.save(highlighted_place1)
            self.repository.save(highlighted_place2)

            highlighted_places = self.repository.get_all()

            expect(highlighted_places).to(contain(highlighted_place1))
            expect(highlighted_places).to(contain(highlighted_place2))