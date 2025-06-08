class Solution:
    def countPermutations(self, c: List[int]) -> int:
        n = len(c)
        for i in range(1, n):
            if c[i] <= c[0]:
                return 0
        ret = 1
        MOD = 10**9+7
        for i in range(1, n):
            ret *= i
            ret %= MOD
        return ret