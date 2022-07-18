import unittest
from pathlib import Path

from day_7.crabs import Crabs
from reader.file_reader import Reader


class TestCrabs(unittest.TestCase):
    def test_one_crab_at_1_fuel_cost_is_zero(self):
        self.assertEqual(0, Crabs([1]).cost_1())

    def test_2_crabs_fuel_cost_is_position_difference(self):
        self.assertEqual(3, Crabs([1, 4]).cost_1())
        self.assertEqual(3, Crabs([7, 4]).cost_1())

    def test_3_crabs_1_2_3_fuel_cost_is_2(self):
        self.assertEqual(2, Crabs([1, 2, 3]).cost_1())

    def test_3_crabs_1_2_4_fuel_cost_is_3(self):
        self.assertEqual(3, Crabs([1, 2, 4]).cost_1())

    def test_example(self):
        file = Path.cwd() / ".." / "day_7" / "example"
        positions = [int(n) for n in Reader(file).lines()[0].split(",")]
        self.assertEqual(37, Crabs(positions).cost_1())

    def test_example2(self):
        file = Path.cwd() / ".." / "day_7" / "example"
        positions = [int(n) for n in Reader(file).lines()[0].split(",")]
        self.assertEqual(168, Crabs(positions).cost_2())



