import unittest

from day_2.submarine import Submarine


class Diver(unittest.TestCase):
    def test_diver_stays_put_with_empty_commands(self):
        self.assertEqual((0, 0), Submarine().move([]))

    def test_diver_can_dive(self):
        self.assertEqual((0, 1), Submarine().move([("down", 1)]))

    def test_diver_can_go_forward(self):
        self.assertEqual((1, 0), Submarine().move([("forward", 1)]))

    def test_diver_can_go_down_and_up(self):
        self.assertEqual((0, 1), Submarine().move([("down", 2), ("up", 1)]))

    def test_diver_can_go_down_and_forward(self):
        self.assertEqual((1, 2), Submarine().move([("down", 2), ("forward", 1)]))

    def test_diver_can_go_anywhere(self):
        commands= [('forward', 2), ('down', 2), ('forward', 6), ('forward', 8), ('down', 8)]
        self.assertEqual((16, 10), Submarine().move(commands))
