import unittest

from main import Truck


class TestTruckMetods(unittest.TestCase):
    """Класс для тестирования класса Truck"""
    print("Test for Truck class")

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.truck1 = Truck('RU', 'MAN', 'diesel', '6*2', 10000)

    def test_lbs_to_kg_converter(self):
        self.assertEqual(Truck.lbs_to_kg_converter(1000), f"1000 lbs = 453.592 kg")

    def test_check_max_weight(self):
        self.assertEqual(Truck.check_max_weight(1000), f"Car weight not in truck weight range")
        self.assertNotEqual(Truck.check_max_weight(3500), f"Car weight not in truck weight range")

    def test_set_max_weight(self):
        with self.assertRaises(ValueError):
            self.truck1.set_max_weight(3400)

    def test_set_chassis_type(self):
        with self.assertRaises(ValueError):
            self.truck1.set_chassis_type('6*6')
