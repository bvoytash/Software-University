from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        for obj in self.cards:
            if obj.name == card.name:
                raise ValueError(f"Card {obj.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        current_card = [obj for obj in self.cards if obj.name == card][0]
        self.cards.remove(current_card)
        self.count -= 1

    def find(self, name: str):
        current_card = [c for c in self.cards if c.name == name][0]
        return current_card
