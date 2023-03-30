class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dp(a, b, c, d):
            f = defaultdict(int)
            for i in range(a, b):
                f[s1[i]] += 1
            for i in range(c, d):
                f[s2[i]] -= 1
            for k in f:
                if f[k] != 0:
                    return False
            if b-a == 1:
                return True
            for x in range(1, b-a):
                if dp(a, a+x, c, c+x) and dp(a+x, b, c+x, d):
                    return True
                if dp(a, a+x, d-x, d) and dp(a+x, b, c, d-x):
                    return True
            return False
        return dp(0, len(s1), 0, len(s1))