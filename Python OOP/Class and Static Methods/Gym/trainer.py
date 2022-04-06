class Trainer:
    id = 0

    def __init__(self, name):
        self.name = name
        Trainer.id += 1
        self.id = Trainer.id

    @staticmethod
    def get_next_id():
        return Trainer.id + 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"