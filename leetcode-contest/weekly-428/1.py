class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        idx = inf
        mx = -inf
        cur = 0
        for i, x in events:
            if x - cur > mx:
                mx = x - cur
                idx = i
            elif x - cur == mx:
                idx = min(idx, i)
            cur = x
        return idx