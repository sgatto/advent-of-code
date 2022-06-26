import unittest

from day_2.submarine import Submarine


class TestSubmarineSimpleMove(unittest.TestCase):
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
        commands = [('forward', 2), ('down', 2), ('forward', 6), ('forward', 8), ('up', 8), ('forward', 8), ('down', 8)]
        self.assertEqual((24, 2), Submarine().move(commands))


class SubmarineAdvancedMove(unittest.TestCase):

    def test_with_empty_commands_submarine_stays_put(self):
        self.assertEqual((0, 0), Submarine().advanced_move([]))

    def test_with_forward_commands_only_submarine_moves_forward(self):
        sub = Submarine()
        self.assertEqual((1, 0), sub.advanced_move([("forward", 1)]))
        self.assertEqual((4, 0), sub.advanced_move([("forward", 1), ("forward", 2)]))

    def test_with_down_or_up_commands_only_submarine_stays_put(self):
        self.assertEqual((0, 0), Submarine().advanced_move([("down", 1)]))
        self.assertEqual((0, 0), Submarine().advanced_move([("up", 1)]))

    def test_with_down_plus_forward_commands_submarine_dives_and_avances(self):
        move = 2
        dive = 3
        self.assertEqual((move, dive * move), Submarine().advanced_move([("down", 3), ("forward", 2)]))

    def test_vertical_aim_accelerates_with_successive_downs(self):
        commands = [("down", 2), ("down", 4), ("up", 1), ("forward", 2)]
        self.assertEqual((2, 10), Submarine().advanced_move(commands))
        commands = [("forward", 5),
                    ("down", 5),
                    ("forward", 8),
                    ("up", 3),
                    ("down", 8),
                    ("forward", 2)]
        self.assertEqual((15, 60), Submarine().advanced_move(commands))
