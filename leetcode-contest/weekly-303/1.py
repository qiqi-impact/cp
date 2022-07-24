class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
            if d[c] == 2:
                return c