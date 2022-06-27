import unittest
from pathlib import Path

import numpy as np

from day_3.binary_diagnostic import BinaryDiagnostic
from reader.file_reader import Reader


class TestGammaEpsilonBinaryDiagnostic(unittest.TestCase):

    def test_gamma_rate_of_1_is_1(self):
        readings = [[1]]
        self.assertEqual(1, BinaryDiagnostic(readings).gamma_rate())

    def test_epsilon_of_1_is_0(self):
        readings = [[1]]
        self.assertEqual(0, BinaryDiagnostic(readings).epsilon())

    def test_gamma_rate_of_11_is_3(self):
        readings = [[1, 1]]
        self.assertEqual(3, BinaryDiagnostic(readings).gamma_rate())

    def test_gamma_rate_of_11_10_00_is_2(self):
        readings = [[1, 1], [1, 0], [0, 0]]
        self.assertEqual(2, BinaryDiagnostic(readings).gamma_rate())

    def test_epsilon_of_11_10_10_00_is_1(self):
        readings = [[1, 1], [1, 0], [0, 0]]
        self.assertEqual(1, BinaryDiagnostic(readings).epsilon())

    def test_examples(self):
        file = Path.cwd() / ".." / "day_3" / "example"
        epsilon = BinaryDiagnostic(Reader(file).digits()).epsilon()
        gamma_rate = BinaryDiagnostic(Reader(file).digits()).gamma_rate()
        self.assertEqual(22, gamma_rate)
        self.assertEqual(9, epsilon)


class TestOxygenCO2BinaryDiagnostic(unittest.TestCase):

    def test_oxygen_gen_rating_of_1_is_1(self):
        readings = [[1]]
        self.assertEqual(1, BinaryDiagnostic(readings).oxygen_gen_rating())

    def test_oxygen_gen_rating_of_1_0_0_is_0(self):
        readings = [[1], [0], [0]]
        self.assertEqual(0, BinaryDiagnostic(readings).oxygen_gen_rating())

    def test_oxygen_gen_rating_of_10_01_00_is_1(self):
        readings = [[1,0], [0,1], [0,0]]
        self.assertEqual(1, BinaryDiagnostic(readings).oxygen_gen_rating())

    def test_co2_scrubber_of_1_is_0(self):
        readings = [[1], [0]]
        self.assertEqual(0, BinaryDiagnostic(readings).co2_scrubber())

    def test_aco2_scrubber_of_10_01_00_is_2(self):
        readings = [[1,0], [0,1], [0,0]]
        self.assertEqual(2, BinaryDiagnostic(readings).co2_scrubber())

    def test_examples(self):
        file = Path.cwd() / ".." / "day_3" / "example"
        oxygen_gen_rating = BinaryDiagnostic(Reader(file).digits()).oxygen_gen_rating()
        co2_scrubber = BinaryDiagnostic(Reader(file).digits()).co2_scrubber()
        self.assertEqual(23, oxygen_gen_rating)
        self.assertEqual(10, co2_scrubber)