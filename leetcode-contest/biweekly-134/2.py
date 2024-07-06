class Solution:
    def maximumPoints(self, e: List[int], c: int) -> int:
        e.sort()
        c -= e[0]
        if c < 0:
            return 0
        x = e[0]
        s = sum(e)
        cur = c + s - x
        return cur // x + 1
        