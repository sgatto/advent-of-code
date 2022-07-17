import unittest
from pathlib import Path

import numpy as np

from day_6.fish_population import FishPopulation
from reader.file_reader import Reader


class TestLantern(unittest.TestCase):
    def test_one_fish2_after_one_day_is_one_fish1(self):
        self.assertEqual([1], FishPopulation([2]).evolve(1))

    def test_fish_2_1_after_one_day_is_1_0(self):
        self.assertEqual([1, 0], FishPopulation([2, 1]).evolve(1))

    def test_fish_3_2_after_2_days_is_1_0(self):
        self.assertEqual([1, 0], FishPopulation([3, 2]).evolve(2))

    def test_fish_2_1_after_2_days_is_0_6_8(self):
        self.assertEqual([0, 6, 8], FishPopulation([2, 1]).evolve(2))

    def test_multiple_iterations_after_a_newborn(self):
        self.assertEqual([6, 5, 7, 8], FishPopulation([1, 0]).evolve(2))

    def test_example(self):
        file = Path.cwd() / ".." / "day_6" / "example"
        fish = [int(n) for n in Reader(file).lines()[0].split(",")]
        self.assertEqual(26, FishPopulation(fish).n_fish_after(18))
        self.assertEqual(5934, FishPopulation(fish).n_fish_after(80))
        self.assertEqual(5934, FishPopulation(fish).n_fish_after_bis(80))

    def test_one_fish_population_after_7_iterations_gives_2(self):
        self.assertEqual(2, FishPopulation([0]).n_fish_after_bis(7))
        self.assertEqual(2, FishPopulation([1]).n_fish_after_bis(7))
        self.assertEqual(2, FishPopulation([2]).n_fish_after_bis(7))
        self.assertEqual(2, FishPopulation([3]).n_fish_after_bis(7))
        self.assertEqual(2, FishPopulation([4]).n_fish_after_bis(7))
        self.assertEqual(2, FishPopulation([5]).n_fish_after_bis(7))
        self.assertEqual(2, FishPopulation([6]).n_fish_after_bis(7))

    def test_one_fish6_population_after_14_iterations_gives_3(self):
        self.assertEqual(3, FishPopulation([6]).n_fish_after_bis(14))

    def test_one_fish4_population_after_14_iterations_gives_4(self):
        self.assertEqual(4, FishPopulation([4]).n_fish_after_bis(14))

    def test_example_long(self):
        file = Path.cwd() / ".." / "day_6" / "example"
        fish = [int(n) for n in Reader(file).lines()[0].split(",")]
        self.assertEqual(26984457539, FishPopulation(fish).n_fish_after_bis(256))
