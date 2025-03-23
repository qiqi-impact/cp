class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(maxWeight // w, n * n)