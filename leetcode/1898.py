class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def can(x):
            r = set(removable[:x])
            pi = 0
            for i, c in enumerate(s):
                if i in r:
                    continue
                if s[i] == p[pi]:
                    pi += 1
                    if pi == len(p):
                        return True
            return False
        l, r = 0, len(removable)
        while l < r:
            mi = (l+r+1)//2
            if can(mi):
                l = mi
            else:
                r = mi - 1
        return l