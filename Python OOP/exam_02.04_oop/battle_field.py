from project.player.advanced import Advanced
from project.player.player import Player
from project.player.beginner import Beginner


class BattleField:
    # @staticmethod
    def fight(self, attacker, enemy):

        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == "Beginner":
            attacker.health += 40
            for obj in attacker.card_repository.cards:
                obj.damage_points += 30

        if enemy.__class__.__name__ == "Beginner":
            enemy.health += 40
            for obj in enemy.card_repository.cards:
                obj.damage_points += 30

        for c in attacker.card_repository.cards:
            attacker.health += c.health_points

        for c in enemy.card_repository.cards:
            enemy.health += c.health_points

        for c in attacker.card_repository.cards:
            enemy.take_damage(c.damage_points)
            if enemy.is_dead:
                enemy.health = 0
                return

        for c in enemy.card_repository.cards:
            attacker.take_damage(c.damage_points)
            if attacker.is_dead:
                attacker.health = 0
                return



# p1 = Beginner("boro")
# p2 = Advanced("pesho")
# a = BattleField()
# a.fight(p1, p2)

