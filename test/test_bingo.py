import unittest
from pathlib import Path

import numpy as np

from day_4.bingo import Board, BingoGame
from reader.bingo_reader import BingoReader
from reader.file_reader import Reader


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board([[22, 13, 17, 11, 0],
                            [8, 2, 23, 4, 24],
                            [21, 9, 14, 16, 7],
                            [6, 10, 3, 18, 5],
                            [1, 12, 20, 15, 19]])

    def test_after_one_extraction_no_win(self):
        self.assertEqual(0, self.board.draw(22))

    def test_board_wins_if_one_full_line_is_extracted_score_is_product_of_non_marked_numbers(self):
        draws = [8, 2, 23, 4]
        self.draw_all(draws)
        score = 22 + 13 + 17 + 11 + 0 + 21 + 9 + 14 + 16 + 7 + 6 + 10 + 3 + 18 + 5 + 1 + 12 + 20 + 15 + 19
        self.assertEqual(score, self.board.draw(24))

    def test_board_wins_if_one_full_column_is_drawn_score_is_product_of_non_marked_numbers(self):
        draws = [13, 2, 9, 10]
        self.draw_all(draws)
        score = 22 + 17 + 11 + 0 + 8 + 23 + 4 + 24 + 21 + 14 + 16 + 7 + 6 + 3 + 18 + 5 + 1 + 20 + 15 + 19
        self.assertEqual(score, self.board.draw(12))

    def draw_all(self, draws):
        for number in draws:
            self.board.draw(number)

    def test_board_score_is_correctly_calculated_wins_if_one_full_column_is_drawn(self):
        all_but_diagonal = [8, 21, 6, 1, 13, 9, 10, 12, 17, 23, 3, 20, 11, 4, 16, 15, 0, 24, 7, 5]
        self.draw_all(all_but_diagonal)

        score = 2 + 14 + 18 + 19
        self.assertEqual(score, self.board.draw(22))


class TestBingoGame(unittest.TestCase):
    def setUp(self) -> None:
        self.board1 = [[1, 2, 3, 4, 5],
                       [6, 7, 8, 9, 10],
                       [11, 12, 13, 14, 15],
                       [16, 17, 18, 19, 20],
                       [21, 22, 23, 24, 25]]
        self.board2 = [[26, 27, 28, 29, 30],
                       [31, 32, 33, 34, 35],
                       [36, 37, 38, 39, 40],
                       [41, 42, 43, 44, 45],
                       [46, 47, 48, 49, 50]]
        self.game = BingoGame([self.board1, self.board2])

    def test_game_2win_has_no_wins_with_one_draw(self):
        draws = [22]
        self.assertEqual(0, self.game.play2win(draws))

    def test_the_winning_score_is_first_board_to_win_score_times_last_drawn_number(self):
        draws = [1, 2, 3, 4, 5]
        sum_numbers_boards1 = np.sum(np.array(self.board1))
        boards_1_score = sum_numbers_boards1 - sum(draws)
        last_draw = draws[-1]
        score = boards_1_score * last_draw
        self.assertEqual(score, self.game.play2win(draws))

    def test_examples_game_to_win(self):
        file = Path.cwd() / ".." / "day_4" / "example"
        boards = BingoReader(Reader(file).lines()).boards()
        draws = BingoReader(Reader(file).lines()).draws()
        game = BingoGame(boards)
        self.assertEqual(4512, game.play2win(draws))

    def test_game_2lose_has_no_wins_with_one_draw(self):
        draws = [22]
        self.assertEqual(0, self.game.play2lose(draws))

    def test_game_2lose_last_board_score_is_selected(self):
        draws_for_boards1_to_win = [1, 2, 3, 4, 5]
        draws_for_boards2_to_win = [31, 32, 33, 34, 35]
        draws = draws_for_boards1_to_win + draws_for_boards2_to_win

        sum_numbers_boards2 = np.sum(np.array(self.board2))
        boards_2_score = sum_numbers_boards2 - sum(draws_for_boards2_to_win)
        last_draw = draws[-1]
        score = boards_2_score * last_draw
        self.assertEqual(score, self.game.play2lose(draws))

    def test_examples_game_to_lose(self):
        file = Path.cwd() / ".." / "day_4" / "example"
        boards = BingoReader(Reader(file).lines()).boards()
        draws = BingoReader(Reader(file).lines()).draws()
        game = BingoGame(boards)
        self.assertEqual(1924, game.play2lose(draws))

