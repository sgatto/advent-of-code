from pathlib import Path

import reader.file_reader
from submarine import Submarine

if __name__ == '__main__':
    file = Path.cwd() / "input-2"
    commands = reader.file_reader.Reader(file).commands()
    (x, p) = Submarine().move(commands)
    print(f"day2-1 : {x*p}")

    (x, p) = Submarine().advanced_move(commands)
    print(f"day2-2 : {x*p}")
