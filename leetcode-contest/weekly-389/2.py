class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        x = s.count(c)
        return x * (x+1) // 2