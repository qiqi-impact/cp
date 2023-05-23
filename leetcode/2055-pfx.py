class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        left = [0] * len(s)
        right = [0] * len(s)

        cur = -1
        for i in range(len(s)):
            if s[i] == '|':
                cur = i
            left[i] = cur

        cur = len(s)
        for i in range(len(s)-1, -1, -1):
            if s[i] == '|':
                cur = i
            right[i] = cur

        pf = [0]
        for c in s:
            pf.append(pf[-1] + int(c == '*'))

        ret = []
        for x, y in queries:
            l = right[x]
            r = left[y]
            ret.append(max(0, pf[r+1] - pf[l]))
        return ret