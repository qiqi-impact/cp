import numpy as np

class MatrixFastPower:
    def __init__(self):
        return

    @staticmethod
    def _matrix_mul(a, b, mod=10**9+7):
        return a @ b % mod

    def matrix_pow(self, base, p, mod=10**9+7):
        ans = np.eye(base.shape[0], dtype=base.dtype)
        while p:
            if p & 1:
                ans = self._matrix_mul(ans, base, mod)
            base = self._matrix_mul(base, base, mod)
            p >>= 1
        return ans