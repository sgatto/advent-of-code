import tempfile
import unittest

from reader.file_reader import Reader


class ReaderTest(unittest.TestCase):
    def test_simple_file(self):
        self.test_dir = tempfile.mkdtemp()
        file = tempfile.mktemp()
        with open(file, "w") as f:
            f.write("1\n2\n3")
        self.assertEqual([1, 2, 3], Reader(file).depth_readings())

    def test_movement_readings(self):
        self.test_dir = tempfile.mkdtemp()
        file = tempfile.mktemp()
        with open(file, "w") as f:
            f.write("for 1\nd 2\nup 3")
        self.assertEqual(["for 1", "d 2", "up 3"], Reader(file).lines())
        self.assertEqual([("for", 1), ("d", 2), ("up", 3)], Reader(file).commands())

    def test_list_of_list_from_digits(self):
        content = "000\n" \
                  "110\n" \
                  "111\n"
        self.test_dir = tempfile.mkdtemp()
        file = tempfile.mktemp()
        with open(file, "w") as f:
            f.write(content)
        expected = [[0, 0, 0],
                    [1, 1, 0],
                    [1, 1, 1]]
        self.assertEqual(expected, Reader(file).digits())
