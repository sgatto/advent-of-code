from pathlib import Path

from day_7.crabs import Crabs
from reader.file_reader import Reader

if __name__ == '__main__':
    file = Path.cwd() / "input"
    positions = [int(n) for n in Reader(file).lines()[0].split(",")]
    print(f"day 7_1: {Crabs(positions).cost_1()}")
    print(f"day 7_2: {Crabs(positions).cost_2()}")
