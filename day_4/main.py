from pathlib import Path

from day_4.bingo import BingoGame
from reader.bingo_reader import BingoReader
from reader.file_reader import Reader

if __name__ == '__main__':
    file = Path.cwd() / "input"
    boards = BingoReader(Reader(file).lines()).boards()
    draws = BingoReader(Reader(file).lines()).draws()
    game = BingoGame(boards)
    print(f"day 4_1: {game.play2win(draws)}")
    print(f"day 4_2: {game.play2lose(draws)}")

