class Solution:
    def solve(self, r, c):
        ret = 0
        for i in range(1, min(r, c)):
            ret += i * (r-i) * (c-i)
            ret %= (10**9+7)
        return ret