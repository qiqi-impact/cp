class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        mni = inf
        mx = -inf
        cur = 0
        for i, x in events:
            if x - cur > mx:
                mx = x - cur
                mni = i
            elif x - cur == mx:
                mni = min(mni, i)
            cur = x
        return mni