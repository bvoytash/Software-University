from project.card.card import Card


class TrapCard(Card):
    # damage_points = 120
    # health_points = 5

    def __init__(self,name: str):
        super().__init__(name, 120, 5)