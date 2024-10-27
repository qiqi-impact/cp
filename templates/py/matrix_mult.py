def mat_mul(X, Y):
    result = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

class MatrixFastPower:
    def __init__(self):
        return

    @staticmethod
    def _matrix_mul(a, b, mod=10 ** 9 + 7):
        n = len(a)
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[i][j] = sum(a[i][k] * b[k][j] for k in range(n)) % mod
        return res

    def matrix_pow(self, base, p, mod=10 ** 9 + 7):
        n = len(base)
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            ans[i][i] = 1
        while p:
            if p & 1:
                ans = self._matrix_mul(ans, base, mod)
            base = self._matrix_mul(base, base, mod)
            p >>= 1
        return ans