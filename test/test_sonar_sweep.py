import unittest

from day_1.sonaranalyser import n_increases, sum_3_items_filter


class SonarSweepTest(unittest.TestCase):
    def test_sonar_sweep_return_zero_with_no_reading(self):
        self.assertEqual(0, n_increases([]))
        self.assertEqual(0, n_increases([1]))

    def test_sonar_sweep_return_one_with_two_increasing_readings(self):
        self.assertEqual(1, n_increases([1, 2]))

    def test_sonar_sweep_return_one_with_1_3_2_readings(self):
        self.assertEqual(1, n_increases([1, 3, 2]))

    def test_filtered_increases_of_three_values_is_zero(self):
        self.assertEqual(0, n_increases(sum_3_items_filter([1, 2, 3]) ) )

    def test_filtered_increases_of_1_2_3_4_is_1(self):
        self.assertEqual(1, n_increases(sum_3_items_filter([1, 2, 3, 4])))


class TestFilter(unittest.TestCase):
    def test_filter_of_3_values_is_the_sum_of_the_three_values(self):
        self.assertEqual([6], sum_3_items_filter([1, 2, 3]))

    def test_filter_of_1_2_3_4_values_is_6_9(self):
        self.assertEqual([6,9], sum_3_items_filter([1, 2, 3, 4]))


