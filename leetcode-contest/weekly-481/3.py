from sortedcontainers import SortedList

class Solution:
    def minSwaps(self, a: List[int], f: List[int]) -> int:
        n = len(a)
        d = defaultdict(int)
        for i in range(n):
            d[a[i]] += 1
            d[f[i]] += 1
        for k in d:
            if d[k] > n:
                return -1
        ct = 0
        e = defaultdict(int)
        for i in range(n):
            if a[i] == f[i]:
                ct += 1
                e[a[i]] += 1

        sl = SortedList()
        for k in e:
            sl.add(e[k])

        ret = 0
        while sl:
            if len(sl) == 1:
                ret += sl[0]
                break
            a = sl.pop(0)
            b = sl.pop(len(sl) - 1)
            if a > b:
                ret += b
                sl.add(a - b)
            elif a < b:
                ret += a
                sl.add(b - a)
            else:
                ret += a
        return ret