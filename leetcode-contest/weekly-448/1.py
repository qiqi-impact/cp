class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        ct = list(Counter(s).values())
        ct.sort(reverse=True)
        return sum(ct[k:])