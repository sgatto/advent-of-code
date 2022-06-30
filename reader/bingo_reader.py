from typing import List


class BingoReader:
    def __init__(self, lines):
        self.lines: List[str] = lines

    def draws(self):
        return [int(n) for n in self.lines[0].split(",")]

    def boards(self):
        boards = []
        for i in range(2,len(self.lines), 6):
            board = []
            for l in range(5):
                board.append([int(n) for n in self.lines[i + l].split()])
            boards.append(board)
        return boards
