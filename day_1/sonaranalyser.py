from typing import List


def n_increases(readings: List):
    return sum([(readings[i] > readings[i - 1]) for i in range(1, len(readings))])


def sum_3_items_filter(data):
    filter_span = 3
    r_range = len(data) - (filter_span - 1)
    return [sum(data[i:i + filter_span]) for i in range(r_range)]


