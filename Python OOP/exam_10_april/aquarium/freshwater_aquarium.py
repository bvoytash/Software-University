from exam_10_april.aquarium.base_aquarium import BaseAquarium

class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name):
        super().__init__(name, 50)