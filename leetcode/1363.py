class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        md = 0
        d = [[] for _ in range(3)]
        for x in digits:
            xx = int(x)
            d[xx%3].append(xx)
            md += xx
            md %= 3
        for i in range(3):
            d[i].sort()
        if md == 2:
            if len(d[2]) >= 1:
                d[2] = d[2][1:]
            else:
                d[1] = d[1][2:]
        elif md == 1:
            if len(d[1]) >= 1:
                d[1] = d[1][1:]
            else:
                d[2] = d[2][2:]
        if not d[2] and not d[1]:
            if not d[0]:
                return ''
            if d[0][-1] == 0:
                return '0'
        ret = ''
        while d[0] or d[1] or d[2]:
            cur = -1
            idx = None
            for i in range(3):
                if d[i] and d[i][-1] > cur:
                    cur = d[i][-1]
                    idx = i
            ret += str(d[idx].pop())
        return ret


