from typing import List

import numpy as np

START_VALUE = 6
STOP_VALUE = 0
NEWBORN_VALUE = 8


class FishPopulation:
    def __init__(self, fish: List[int]):
        self.population = np.array(fish, dtype=np.int64)
        self.stored = {}

    def evolve(self, days: int):
        for _ in range(days):
            self._one_iteration()
        return self.population.tolist()

    def _one_iteration(self):
        n_new_fish = self._decrease_values()
        self._add_newborns(n_new_fish)

    def _decrease_values(self):
        self.population -= 1
        n_new_fish = np.sum(self.population < STOP_VALUE)
        self.population = np.where(self.population < STOP_VALUE, START_VALUE, self.population)
        return n_new_fish

    def _add_newborns(self, n_new_fish):
        new_fish = np.full(n_new_fish, NEWBORN_VALUE, dtype=int)
        self.population = np.append(self.population, new_fish)

    def n_fish_after(self, days: int):
        self.evolve(days)
        return len(self.population)

    def n_fish_after_bis(self, days):
        n_fish = 0
        for f in self.population:
            n_fish += 1
            n_fish += self._fish6_n_sons(days + (6 - f))
        return n_fish

    def _fish6_n_sons(self, n_days):
        if n_days not in self.stored:
            fish6_n_sons = n_days // 7
            for days_left in range(n_days-7-2, 0, -7):
                fish6_n_sons += self._fish6_n_sons(days_left)
            self.stored[n_days] = fish6_n_sons
        return self.stored[n_days]

