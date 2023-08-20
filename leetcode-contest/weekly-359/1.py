class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        x = ''
        for w in words:
            x += w[0]
        return s == x