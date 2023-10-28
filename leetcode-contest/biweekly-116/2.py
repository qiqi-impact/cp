class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        for i in range(0, len(s) - 1, 2):
            if s[i + 1] != s[i]:
                changes += 1
                
        return changes