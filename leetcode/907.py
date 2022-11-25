from sortedcontainers import SortedList

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        l = [(arr[i], i) for i in range(n)]
        l.sort()
        sl = SortedList([-1, n])
        ret = 0
        for v, i in l:
            idx = sl.bisect_left(i)
            a, b = sl[idx-1], sl[idx]
            ret += v * (i - a) * (b - i)
            ret %= int(10**9+7)
            sl.add(i)
        return ret