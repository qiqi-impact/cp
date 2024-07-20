class Solution:
    def minimumLength(self, s: str) -> int:
        d = defaultdict(int)
        for x in s:
            d[x] += 1
        ret = 0
        for k in d:
            ret += 1 if d[k]%2 else 2
        return ret