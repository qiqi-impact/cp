class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        pf = [0]
        bars = []
        for i, c in enumerate(s):
            df = int(c == '*')
            pf.append(pf[-1] + df)
            if c == '|':
                bars.append(i)
        ret = []
        for x, y in queries:
            l = bisect.bisect_left(bars, x)
            r = bisect.bisect_right(bars, y) - 1
            if r < l:
                ret.append(0)
            else:
                ret.append(pf[bars[r]+1] - pf[bars[l]+1])
        return ret