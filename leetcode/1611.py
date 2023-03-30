class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def f(x):
            if x <= 1:
                return x
            mx = 0
            for i in range(31, -1, -1):
                if (1 << i) & x:
                    mx = i
                    break
            return 2 ** (mx+1) - 1 - f(x ^ (1 << mx))
        return f(n)