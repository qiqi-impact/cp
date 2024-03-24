class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        ret = 0
        for i in range(n):
            d = defaultdict(int)
            for j in range(i, n):
                d[s[j]] += 1
                if d[s[j]] <= 2:
                    ret = max(ret, j - i + 1)
                else:
                    break
        return ret