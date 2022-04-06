from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_hard = PowerHardware(name, capacity, memory)
        System._hardware.append(new_hard)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_hard = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_hard)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        flag = False
        for obj in System._hardware:
            if obj.name == hardware_name:
                flag = True
                new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
                try:
                    obj.install(new_software)
                    System._software.append(new_software)
                except:
                    return "Software cannot be installed"
        if not flag:
            return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        flag = False
        for obj in System._hardware:
            if obj.name == hardware_name:
                flag = True
                new_software = LightSoftware(name, capacity_consumption, memory_consumption)
                try:
                    obj.install(new_software)
                    System._software.append(new_software)

                except:
                    return "Software cannot be installed"
        if not flag:
            return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        current_hard = None
        current_soft = None
        for obj in System._hardware:
            if obj.name == hardware_name:
                current_hard = obj
        for obj in System._software:
            if obj.name == software_name:
                current_soft = obj

        if current_soft and current_hard:
            current_hard.uninstall(current_soft)
            System._software.remove(current_soft)
        else:
            return "Some of the components do not exist"


    @staticmethod
    def analyze():
        total_memory = sum([obj.memory for obj in System._hardware])
        total_capacity = sum([obj.capacity for obj in System._hardware])
        used_memory = sum([obj.memory_consumption for obj in System._software])
        used_capacity = sum([obj.capacity_consumption for obj in System._software])
        return "System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {used_memory} / {total_memory}\n" \
               f"Total Capacity Taken: {used_capacity} / {total_capacity}"

    @staticmethod
    def system_split():
        return
