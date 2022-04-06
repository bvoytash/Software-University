class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        message = []
        message.append(f"Player: {self.name}")
        message.append(f"Sprint: {self.__sprint}")
        message.append(f"Dribble: {self.__dribble}")
        message.append(f"Passing: {self.__passing}")
        message.append(f"Shooting: {self.__shooting}")
        return "\n".join(message)