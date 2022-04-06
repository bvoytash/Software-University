from project.card.card import Card


class MagicCard(Card):
    # damage_points = 5
    # health_points = 80

    def __init__(self,name: str):
        super().__init__(name, 5, 80)

