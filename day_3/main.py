from pathlib import Path

import numpy as np

import binary_diagnostic
from reader.file_reader import Reader

if __name__ == '__main__':
    file = Path.cwd() / "input-3"
    epsilon = binary_diagnostic.BinaryDiagnostic(Reader(file).digits()).epsilon()
    gamma_rate = binary_diagnostic.BinaryDiagnostic(Reader(file).digits()).gamma_rate()
    print(epsilon*gamma_rate)
    oxygen_gen_rating = binary_diagnostic.BinaryDiagnostic(Reader(file).digits()).oxygen_gen_rating()
    co2_scrubber = binary_diagnostic.BinaryDiagnostic(Reader(file).digits()).co2_scrubber()
    print(oxygen_gen_rating * co2_scrubber)
