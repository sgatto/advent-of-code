import pathlib
import tempfile
import unittest

from reader.bingo_reader import BingoReader
from reader.file_reader import Reader


class ReaderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_dir = tempfile.mkdtemp()

    def test_simple_file(self):
        file = tempfile.mktemp()
        with open(file, "w") as f:
            f.write("1\n2\n3")
        self.assertEqual([1, 2, 3], Reader(file).depth_readings())

    def test_movement_readings(self):
        file = tempfile.mktemp()
        with open(file, "w") as f:
            f.write("for 1\nd 2\nup 3")
        self.assertEqual(["for 1", "d 2", "up 3"], Reader(file).lines())
        self.assertEqual([("for", 1), ("d", 2), ("up", 3)], Reader(file).commands())

    def test_list_of_list_from_digits(self):
        content = "000\n" \
                  "110\n" \
                  "111\n"
        file = tempfile.mktemp()
        with open(file, "w") as f:
            f.write(content)
        expected = [[0, 0, 0],
                    [1, 1, 0],
                    [1, 1, 1]]
        self.assertEqual(expected, Reader(file).digits())


class TestBingoReader(unittest.TestCase):
    def test_day_4_example_file(self):
        content = "1,2,42\n" \
                  "\n" \
                  "22 13 17 11  0\n" \
                  "8  2 23  4 24\n" \
                  "21  9 14 16  7\n" \
                  "6 10  3 18  5\n" \
                  "1 12 20 15 19\n" \
                  "\n" \
                  "12 23 17 11  0\n" \
                  "44  2 23  4 24\n" \
                  "12  29 14 16  7\n" \
                  "1 21  3 18  5\n" \
                  "11 22 20 15 19\n"
        file = tempfile.mktemp()
        with open(file, "w") as f:
            f.write(content)
        draws = [1, 2, 42]
        lines = Reader(file).lines()
        self.assertEqual(draws, BingoReader(lines).draws())
        board1 = [[22, 13, 17, 11, 0],
                 [8, 2, 23, 4, 24],
                 [21, 9, 14, 16, 7],
                 [6, 10, 3, 18, 5],
                 [1, 12, 20, 15, 19]]
        board2 = [[12, 23, 17, 11, 0],
                 [44, 2, 23, 4, 24],
                 [12, 29, 14, 16, 7],
                 [1, 21, 3, 18, 5],
                 [11, 22, 20, 15, 19]]
        self.assertEqual(board1, BingoReader(lines).boards()[0])
        self.assertEqual(board2, BingoReader(lines).boards()[1])
