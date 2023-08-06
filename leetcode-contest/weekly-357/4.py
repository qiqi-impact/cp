class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(reverse=True)
        sm = 0
        f = {}
        for i in range(k):
            sm += items[i][0]
            f[items[i][1]] = f.get(items[i][1], 0) + 1
        ct = len(f)
        ret = sm + ct * ct
        tp = k
        for i in range(k-1, -1, -1):
            x, y = items[i]
            if f[y] == 1:
                continue
            f[y] -= 1
            sm -= x
            while 1:
                if tp == len(items):
                    return ret
                a, b = items[tp]
                tp += 1
                if b in f:
                    continue
                break
            f[b] = 1
            sm += a
            ct = len(f)
            ret = max(ret, sm + ct * ct)
        return ret
            