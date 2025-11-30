class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set([c for c in s]))