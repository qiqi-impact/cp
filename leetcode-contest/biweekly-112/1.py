class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        for st in [0, 1]:
            ct = defaultdict(int)
            for i in range(st, len(s1), 2):
                ct[s1[i]] += 1
                ct[s2[i]] -= 1
            for k in ct:
                if ct[k] != 0:
                    return False
        return True