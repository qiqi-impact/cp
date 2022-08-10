class Solution:
    @cache
    def f(a, b):
        MOD = 10**9+7
        if a == b:
            return 1
        if b == 0:
            return 0
        return (Solution.f(a-1, b) * (a-1) + Solution.f(a-1, b-1)) % MOD
    def rearrangeSticks(self, n: int, k: int) -> int:
        return Solution.f(n, k)