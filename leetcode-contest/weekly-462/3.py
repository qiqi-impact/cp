from sortedcontainers import SortedList

class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        l = list(zip(value, limit))
        sl = SortedList()
        l.sort(key=lambda x:(x[1], -x[0]))
        # tot = 0
        # ret = 0
        # taken = []
        # for v, w in l:
        #     if w > tot:
        #         ret += v
        #         taken.append((v, w))
        tot = 0
        # d = defaultdict(list)
        for v, w in l:
            while sl and sl[0][1] < w:
                sl.pop(0)
            # d[w].append(v)
            if len(sl) < w:
                sl.add((v, w))
                tot += v
            elif sl[0][0] < v:
                tot += v - sl[0][0]
                sl.discard(sl[0])
                sl.add((v, w))
            # print(sl)
        return tot©leetcode