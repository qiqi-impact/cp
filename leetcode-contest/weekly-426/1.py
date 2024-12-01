class Solution:
    def smallestNumber(self, n: int) -> int:
        cur = 1
        while cur < n:
            cur = 2 * cur + 1
        return cur