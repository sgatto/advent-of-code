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
        self.assertEqual(["for 1","d 2","up 3"], Reader(file).lines())
        self.assertEqual([("for", 1),("d", 2),("up", 3)], Reader(file).commands())
