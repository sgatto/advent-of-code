import numpy as np


class Crabs:
    def __init__(self, positions):
        self.positions = np.array(positions, dtype=np.int64)
        self.median = np.median(self.positions)
        self.mean = np.mean(self.positions)

    def cost_1(self):
        return self._get_cost_type_1(round(self.median))

    def cost_2(self):
        return self._get_cost_type_2(round(self.mean))

    def _get_cost_type_1(self, center):
        differences = self.positions - center
        abs_diff = abs(differences)
        return np.sum(abs_diff)

    def _get_cost_type_2(self, center):
        differences = self.positions - center
        abs_diff = abs(differences)
        return np.sum(0.5*abs_diff*(abs_diff-1))

