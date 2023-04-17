from src.business.model.forecast import Forecast


class HighlightedPlace:
    def __init__(self, name: str, description: str, coordinates: str, id=None, forecast: Forecast=None):
        self.id = id
        self.name = name
        self.description = description
        self.coordinates = coordinates
        self.forecast = forecast

    def __eq__(self, other):
        if isinstance(other, HighlightedPlace):
            return (self.id, self.name, self.description, self.coordinates) == \
               (other.id, other.name, other.description, other.coordinates)
        return False

    def __repr__(self):
        return f"<HighlightedPlace id={self.id}, name='{self.name}', description='{self.description}', coordinates='{self.coordinates}'>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'coordinates': self.coordinates,
            'forecast': self._forecast_to_dict()
        }

    def _forecast_to_dict(self):
        if self.forecast:
            return self.forecast.to_dict()
        return None
