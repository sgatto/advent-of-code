from pathlib import Path

import reader.file_reader
import sonaranalyser

if __name__ == '__main__':
    input = Path.cwd() / "input-1-1"
    data = reader.file_reader.Reader(input).depth_readings()
    n_increases = sonaranalyser.SonarAnalyser().n_increases(data)
    n_filtered_increases = sonaranalyser.SonarAnalyser().filtered_n_increases(data)
    print(n_increases)
    print(n_filtered_increases)

