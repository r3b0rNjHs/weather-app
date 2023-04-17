from src.business.model.highlighted_place import HighlightedPlace


class CreateHighlightedPlace:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, name, description, coordinates):
        highlighted_place = HighlightedPlace(name=name, description=description, coordinates=coordinates)
        return self.repository.save(highlighted_place)
