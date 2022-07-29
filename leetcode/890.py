class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def checkword(w):
            m = {}
            used = set()
            for i, c in enumerate(w):
                p = pattern[i]
                if p not in m:
                    if c in used:
                        return False
                    m[p] = c
                    used.add(c)
                elif m[p] != c:
                    return False
            return True
        return [w for w in words if checkword(w)]