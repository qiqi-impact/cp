class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ret = 0
        for w in words:
            if s.startswith(w):
                ret += 1
        return ret 