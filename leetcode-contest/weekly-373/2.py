class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ret = 0
        for i in range(n):
            v, c = 0, 0
            for j in range(i, n):
                if s[j] in 'aeiou':
                    v += 1
                else:
                    c += 1
                if v == c and (v*c)%k == 0:
                    ret += 1
        return ret