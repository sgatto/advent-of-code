import numpy as np


class BinaryDiagnostic:
    def __init__(self, readings):
        self.readings = np.flip(np.transpose(np.array(readings)), axis=0)
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
        factors = np.power(np.full(self.n_bits, 2), np.arange(self.n_bits))
        return np.dot(factors, binary_bits)
