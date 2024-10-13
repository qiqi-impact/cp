from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        d = {}
        sl = SortedList()
        for i in range(k):
            v = nums[i]
            d[v] = d.get(v, 0) + 1
        for t in d:
            sl.add((d[t], t))
        sm = 0
        for i in range(len(sl)-x, len(sl)):
            if i >= 0:
                sm += sl[i][0] * sl[i][1]
        ret = [sm]
        for i in range(k, len(nums)):
            v = nums[i]
            p = (d.get(v, 0), v)
            try:
                idx = sl.index(p)
                if idx >= len(sl)-x:
                    sm -= v * d[v]
                    t = len(sl)-x-1
                    if t >= 0:
                        sm += sl[t][0] * sl[t][1]
            except:
                pass
            sl.discard(p)
            d[v] = d.get(v, 0) + 1
            p = (d.get(v, 0), v)
            sl.add(p)
            try:
                idx = sl.index(p)
                if idx >= len(sl)-x:
                    sm += v * d[v]
                    t = len(sl)-x-1
                    if t >= 0:
                        sm -= sl[t][0] * sl[t][1]
            except:
                pass
            j = i - k
            v = nums[j]
            p = (d.get(v, 0), v)
            try:
                idx = sl.index(p)
                if idx >= len(sl)-x:
                    sm -= v * d[v]
                    t = len(sl)-x-1
                    if t >= 0:
                        sm += sl[t][0] * sl[t][1]
            except:
                pass
            sl.discard(p)
            d[v] = d.get(v, 0) - 1
            p = (d.get(v, 0), v)
            sl.add(p)
            try:
                idx = sl.index(p)
                if idx >= len(sl)-x:
                    sm += v * d[v]
                    t = len(sl)-x-1
                    if t >= 0:
                        sm -= sl[t][0] * sl[t][1]
            except:
                pass
            ret.append(sm)
        return ret
