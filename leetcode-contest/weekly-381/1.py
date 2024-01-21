class Solution:
    def minimumPushes(self, word: str) -> int:
        ct = Counter(word)
        l = sorted([(-ct[x], x) for x in ct])
        ret = 0
        ct = 0
        for a, b in l:
            a = -a
            ret += (1+ct//8) * a
            ct += 1
        return ret