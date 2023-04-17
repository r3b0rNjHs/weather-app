import psycopg2
from psycopg2.extras import DictCursor

from src.business.services.highlighted_place_repository import HighlightedPlaceRepository
from src.business.model.highlighted_place import HighlightedPlace


class HighlightedPlacePostgresqlRepository(HighlightedPlaceRepository):
    def __init__(self, conn_string):
        self.conn_string = conn_string

    def save(self, highlighted_place):
        with psycopg2.connect(self.conn_string) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO highlighted_places (name, description, coordinates) VALUES (%s, %s, %s) RETURNING id",
                (highlighted_place.name, highlighted_place.description, highlighted_place.coordinates))
            (highlighted_place_id,) = cursor.fetchone()
            cursor.close()
            highlighted_place.id = highlighted_place_id
            return highlighted_place

    def retrieve_by_id(self, highlighted_place_id):
        with psycopg2.connect(self.conn_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, description, coordinates FROM highlighted_places WHERE id = %s",
                           (highlighted_place_id,))
            row = cursor.fetchone()
            cursor.close()
            if row is not None:
                (id, name, description, coordinates) = row
                return HighlightedPlace(id=id, name=name, description=description, coordinates=coordinates)
            else:
                return None

    def remove(self, highlighted_place):
        with psycopg2.connect(self.conn_string) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM highlighted_places WHERE id = %s", (highlighted_place.id,))
            cursor.close()
            return highlighted_place

    def get_all(self):
        with psycopg2.connect(self.conn_string, cursor_factory=DictCursor) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, description, coordinates FROM highlighted_places")
            result = cursor.fetchall()
            return [HighlightedPlace(id=id, name=name, description=description, coordinates=coordinates)
                    for (id, name, description, coordinates) in result]
