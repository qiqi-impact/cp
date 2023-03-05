class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        cur = 0
        ranges.sort()
        lst = -inf
        for x, y in ranges:
            if x > lst:
                cur += 1
                lst = y
            else:
                lst = max(lst, y)
        return pow(2, cur, 10**9+7)