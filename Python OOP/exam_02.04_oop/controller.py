from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        if type == "Beginner":
            new_player = Beginner(username)
            self.player_repository.add(new_player)
            return f"Successfully added player of type {type} with username: {username}"
        elif type == "Advanced":
            new_player = Advanced(username)
            self.player_repository.add(new_player)
            return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        if type == "Magic":
            new_card = MagicCard(name)
            self.card_repository.add(new_card)
            return f"Successfully added card of type {type}Card with name: {name}"
        elif type == "Trap":
            new_card = TrapCard(name)
            self.card_repository.add(new_card)
            return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        current_user = [u for u in self.player_repository.players if u.username == username][0]
        current_card = [c for c in self.card_repository.cards if c.name == card_name][0]

        current_user.card_repository.cards.append(current_card)
        current_user.card_repository.count += 1
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = [obj for obj in self.player_repository.players if obj.username == attack_name][0]
        enemy = [obj for obj in self.player_repository.players if obj.username == enemy_name][0]
        bf = BattleField()
        bf.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = []
        for obj in self.player_repository.players:
            result.append(f"Username: {obj.username} - Health: {obj.health} - Cards {len(obj.card_repository.cards)}")
            for c in obj.card_repository.cards:
                result.append(f"### Card: {c.name} - Damage: {c.damage_points}")
            return '\n'.join(result)


