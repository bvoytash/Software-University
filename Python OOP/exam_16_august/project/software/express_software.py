from project.software.software import Software


class ExpressSoftware(Software):
    TYPE = "Express"

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Express", capacity_consumption, int(memory_consumption * 2))
        # self.type = ExpressSoftware.TYPE
        # self.memory_consumption = memory_consumption