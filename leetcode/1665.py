class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        t = [(y-x, y) for x, y in tasks]
        t.sort(reverse=True)
        cur = 0
        ret = 0
        for x, y in t:
            if cur < y:
                ret += y - cur
                cur = y
            cur -= y
            cur += x
        return ret