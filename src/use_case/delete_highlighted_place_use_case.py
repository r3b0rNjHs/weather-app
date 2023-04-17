class DeleteHighlightedPlace:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, highlighted_place_id):
        highlighted_place = self.repository.retrieve_by_id(highlighted_place_id)
        return self.repository.remove(highlighted_place)
