from pathlib import Path

from day_6.fish_population import FishPopulation
from reader.file_reader import Reader
from reader.segments_reader import SegmentsReader

if __name__ == '__main__':
    file = Path.cwd() / "input"
    fish = [int(n) for n in Reader(file).lines()[0].split(",")]
    print(f"day 6_1: {len(FishPopulation(fish).evolve(80))}")
    print(f"day 6_1: {FishPopulation(fish).n_fish_after_bis(80)}")
    print(f"day 6_2: {FishPopulation(fish).n_fish_after_bis(256)}")
