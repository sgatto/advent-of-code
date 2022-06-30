import numpy as np


class CloudLines:
    def __init__(self, segments):
        self.lines = [Line(s[0], s[1]) for s in segments]
        npsegments = np.asarray(segments)
        xmax = np.max(npsegments[:, :, 0])
        ymax = np.max(npsegments[:, :, 1])
        self.marked = np.zeros((xmax + 1, ymax + 1), dtype=int)

    def danger_points_v1(self):
        for l in self.lines:
            for point in l.points_v1():
                self.marked[point[0], point[1]] += 1
        return len(np.where(self.marked >= 2)[0])

    def danger_points_v2(self):
        for l in self.lines:
            for point in l.points_v2():
                self.marked[point[0], point[1]] += 1
        return len(np.where(self.marked >= 2)[0])


class Line:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def points_v1(self):
        xa, ya = self.start
        xb, yb = self.stop
        if ya == yb:
            return self.horizontal_line(xa, xb, ya)
        elif xa == xb:
            return self.vertical_line(ya, yb, xa)
        else:
            return []

    def points_v2(self):
        xa, ya = self.start
        xb, yb = self.stop
        if abs(xa-xb) == abs(ya-yb):
            return self.diagonal_line_45_deg(xa, xb, ya, yb)
        else:
            return self.points_v1()

    def diagonal_line_45_deg(self, xa, xb, ya, yb):
        N = abs(xa - xb)
        return self.generic_n_point_line(N, xa, xb, ya, yb)

    def vertical_line(self, ya, yb, x):
        N = abs(ya - yb)
        return self.generic_n_point_line(N, x, x, ya, yb)

    def horizontal_line(self, xa, xb, y):
        N = abs(xa - xb)
        return self.generic_n_point_line(N, xa, xb, y, y)

    def generic_n_point_line(self, N, xa, xb, ya, yb):
        points = [(xa, ya)]
        for i in range(1, N + 1):
            dy = (yb - ya) / N
            dx = (xb - xa) / N
            x = int(xa + i * dx)
            y = int(ya + i * dy)
            points.append((x, y))
        return points
