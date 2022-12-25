class Solution:
    def equalFrequency(self, word: str) -> bool:
        ct = Counter(word)
        for c in word:
            ct[c] -= 1
            s = set(ct.values())
            s.discard(0)
            if len(s) == 1:
                return True
            ct[c] += 1
        return False