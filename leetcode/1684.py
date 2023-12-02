class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ret = 0
        s = set(allowed)
        for w in words:
            fail = 0
            for c in w:
                if c not in s:
                    fail = 1
            if not fail:
                ret += 1
        return ret