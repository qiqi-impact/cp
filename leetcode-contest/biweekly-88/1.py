class Solution:
    def equalFrequency(self, word: str) -> bool:
        d = defaultdict(int)
        for c in word:
            d[c] += 1
        l = list(sorted(d.values()))
        if len(l) == 1:
            return True
        if l[0] == 1 and l[1] == l[-1]:
            return True
        if l[-1] != l[-2] + 1 or l[-2] != l[0]:
            return False
        return True