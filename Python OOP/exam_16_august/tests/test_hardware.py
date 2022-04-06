from unittest import TestCase, main
from project.software.software import Software
from project.hardware.hardware import Hardware


class TestHardware(TestCase):

    def test_init_hard(self):
        self.hard = Hardware(name="Test", type="Light", capacity=100, memory=100)
        self.assertEqual("Test", self.hard.name)
        self.assertEqual("Light", self.hard.type)
        self.assertEqual(100, self.hard.capacity)
        self.assertEqual(100, self.hard.memory)
        self.assertEqual([], self.hard.software_components)

    def test_install_soft(self):
        self.soft = Software("soft", "express", 10, 10)
        self.hard = Hardware(name="Test", type="Light", capacity=100, memory=100)
        self.hard.install(self.soft)
        self.assertEqual(self.soft, self.hard.software_components[0])

    def test_no_memory_for_install(self):
        self.soft = Software("soft", "express", 120, 120)
        self.hard = Hardware(name="Test", type="Light", capacity=100, memory=100)
        with self.assertRaises(Exception) as ex:
            self.hard.install(self.soft)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_uninstall_soft(self):
        self.soft = Software("soft", "express", 10, 10)
        self.hard = Hardware(name="Test", type="Light", capacity=100, memory=100)
        self.hard.install(self.soft)
        self.hard.uninstall(self.soft)
        self.assertEqual([], self.hard.software_components)


if __name__ == "__main__":
    main()