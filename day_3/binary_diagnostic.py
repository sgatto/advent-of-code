import numpy as np


class BinaryDiagnostic:
    def __init__(self, readings):
        self.readings = np.transpose(np.array(readings))
        self.n_bits, self.n_lines = self.readings.shape

    def gamma_rate(self):
        gamma_bits = self._binary_gamma_rate()
        return self._decimal_conversion(gamma_bits)

    def epsilon(self):
        epsilon_bits = np.logical_not(self._binary_gamma_rate())
        return self._decimal_conversion(epsilon_bits)

    def _binary_gamma_rate(self):
        sums = np.sum(self.readings, axis=1)
        gamma_bits = sums >= self.n_lines / 2
        return gamma_bits

    def _decimal_conversion(self, binary_bits):
        power2_factors = np.power(np.full(self.n_bits, 2), np.arange(self.n_bits))
        binary_bits = np.flip(binary_bits, axis=0)
        return np.dot(power2_factors, binary_bits)

    def oxygen_gen_rating(self):
        survivors = self.readings
        for i in range(self.n_bits):
            survivors = self._select_lines_ith_most_common_bit(survivors, i)
        return self._decimal_conversion(survivors[:, 0])

    def co2_scrubber(self):
        survivors = self.readings
        for i in range(self.n_bits):
            survivors = self._select_lines_ith_least_common_bit(survivors, i)
            if survivors.shape[1] == 1:
                break
        return self._decimal_conversion(survivors[:, 0])

    def _select_lines_ith_most_common_bit(self, survivors, i):
        n_lines = survivors.shape[1]
        most_common_value = 1 if np.sum(survivors, axis=1)[i] >= n_lines / 2 else 0
        return self._select_lines_having_ith_bit_equal_to(survivors, most_common_value, i)

    def _select_lines_ith_least_common_bit(self, survivors, i):
        n_lines = survivors.shape[1]
        least_common_value = 0 if np.sum(survivors, axis=1)[i] >= n_lines / 2 else 1
        result = self._select_lines_having_ith_bit_equal_to(survivors, least_common_value, i)
        return result

    def _select_lines_having_ith_bit_equal_to(self, survivors, value, i):
        mask = survivors[i, :] == value
        return survivors[:, mask]
