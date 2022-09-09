from sortedcontainers import SortedList

class Solution:
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        p.sort(key=lambda x:(-x[0], x[1]))
        mx = -float('inf')
        ret = 0
        for x, y in p:
            if mx > y:
                ret += 1
            mx = max(mx, y)
        return ret