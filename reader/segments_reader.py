from typing import List


class SegmentsReader:
    def __init__(self, lines):
        self.lines: List[str] = lines

    def segments(self):
        segments = []
        for line in self.lines:
            points = line.split(" -> ")
            start = tuple([int(coord) for coord in points[0].split(",")])
            stop = tuple([int(coord) for coord in points[1].split(",")])
            segments.append((start, stop))
        return segments
