class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = {}
        for t in tasks:
            d[t] = d.get(t, 0) + 1
        ret = 0
        for k in d:
            if d[k] == 1:
                return -1
            elif d[k] % 3 == 0:
                ret += d[k] // 3
            else:
                ret += d[k] // 3 + 1
        return ret