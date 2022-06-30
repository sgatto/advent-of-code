from typing import List
import numpy as np


class Board:
    def __init__(self, numbers: List[List[int]]):
        self.numbers = np.array(numbers, dtype=int)
        self.not_marked = np.ones(self.numbers.shape, dtype=int)
        self.draws = []

    def draw(self, draw):
        self._update_marked(draw)
        if self.win_by_complete_axis(0) or self.win_by_complete_axis(1):
            return np.sum(self.numbers * self.not_marked)
        return False

    def win_by_complete_axis(self, axis):
        n_marked_on_axis = np.sum(self.not_marked, axis=axis)
        winning_axis = np.where(n_marked_on_axis == 0)
        return winning_axis[0].size > 0

    def _update_marked(self, draw):
        indexes = np.where(self.numbers == draw)
        if indexes[0].size > 0:
            i, j = indexes[0][0], indexes[1][0]
            self.not_marked[i][j] = 0


class BingoGame:
    def __init__(self, boards: List[List[List[int]]]):
        self.boards = [Board(numbers) for numbers in boards]

    def play2win(self, draws: List[int]):
        for number in draws:
            for board in self.boards:
                board_score = board.draw(number)
                if board_score > 0:
                    return board_score * number
        return 0

    def play2lose(self, draws):
        winners = []
        for number in draws:
            for i, board in enumerate(self.boards):
                board_score = board.draw(number)
                if board_score > 0:
                    if i not in winners:
                        winners.append(i)
                    if len(winners) == len(self.boards):
                        return board_score * number
        return 0





