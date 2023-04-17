from abc import abstractmethod
from typing import List

from src.business.model.highlighted_place import HighlightedPlace


class HighlightedPlaceRepository:
    @abstractmethod
    def retrieve_by_id(self, highlighted_place_id: str) -> HighlightedPlace:
        pass

    @abstractmethod
    def save(self, highlighted_place: HighlightedPlace) -> HighlightedPlace:
        pass

    @abstractmethod
    def remove(self, highlighted_place: HighlightedPlace) -> HighlightedPlace:
        pass

    @abstractmethod
    def get_all(self) -> List[HighlightedPlace]:
        pass
