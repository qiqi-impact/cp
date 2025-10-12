from sortedcontainers import SortedList

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ret = 0
        for i in range(n):
            ct = defaultdict(int)
            sl = SortedList()
            for j in range(i, n):
                c = s[j]
                if c in ct:
                    sl.discard(ct[c])
                ct[c] += 1
                sl.add(ct[c])
                if sl[0] == sl[-1]:
                    ret = max(ret, j - i + 1)
        return ret