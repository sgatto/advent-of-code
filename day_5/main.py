from pathlib import Path

from day_5.line import CloudLines
from reader.file_reader import Reader
from reader.segments_reader import SegmentsReader

if __name__ == '__main__':
    file = Path.cwd() / "input"
    segments = SegmentsReader(Reader(file).lines()).segments()
    print(f"day 5_1: {CloudLines(segments).danger_points_v1()}")
    print(f"day 5_2: {CloudLines(segments).danger_points_v2()}")
