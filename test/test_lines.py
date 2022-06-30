import unittest
from pathlib import Path

from day_5.line import Line, CloudLines
from reader.file_reader import Reader
from reader.segments_reader import SegmentsReader


class TestLines(unittest.TestCase):
    def test_line_with_start_equal_stop_return_one_covered_point(self):
        start = stop = (0, 0)
        line = Line(start, stop)
        self.assertEqual([(0, 0)], line.points_v1())
        self.assertEqual([(0, 0)], line.points_v2())

    def test_start_stop_on_horizontal_segment(self):
        start = (2, 0)
        stop = (0, 0)
        line = Line(start, stop)
        self.assertEqual([(2, 0), (1, 0), (0, 0)], line.points_v1())
        self.assertEqual([(2, 0), (1, 0), (0, 0)], line.points_v2())

    def test_start_stop_on_vertical_segment(self):
        start = (0, 2)
        stop = (0, 0)
        line = Line(start, stop)
        self.assertEqual([(0, 2), (0, 1), (0, 0)], line.points_v1())
        self.assertEqual([(0, 2), (0, 1), (0, 0)], line.points_v2())

    def test_empty_list_on_45diagonal_segment_v1(self):
        start = (0, 2)
        stop = (2, 0)
        line = Line(start, stop)
        self.assertEqual([], line.points_v1())

    def test_empty_list_on_45diagonal_segment_v2(self):
        start = (0, 2)
        stop = (2, 0)
        line = Line(start, stop)
        self.assertEqual([(0, 2), (1, 1), (2, 0)], line.points_v2())


class TestCloudLines(unittest.TestCase):
    def test_with_one_point_segment_cloudLines_returns_1(self):
        segment = ((1, 2), (1, 2))
        self.assertEqual(0, CloudLines([segment]).danger_points_v1())

    def test_with_one_segment_of_3_points_cloudLines_returns_3(self):
        segment = ((1, 2), (3, 2))
        self.assertEqual(0, CloudLines([segment]).danger_points_v1())

    def test_with_two_segments_with_one_common_point_cloudLines_returns_1(self):
        s1 = ((1, 2), (3, 2))
        s2 = ((1, 2), (1, 8))
        self.assertEqual(1, CloudLines([s1, s2]).danger_points_v1())

    def test_example_returns_5(self):
        file = Path.cwd() / ".." / "day_5" / "example"
        segments = SegmentsReader(Reader(file).lines()).segments()
        self.assertEqual(5, CloudLines(segments).danger_points_v1())

    def test_example_v2_returns_12(self):
        file = Path.cwd() / ".." / "day_5" / "example"
        segments = SegmentsReader(Reader(file).lines()).segments()
        self.assertEqual(12, CloudLines(segments).danger_points_v2())
