class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def can(x):
            rem = [False] * len(s)
            for i in range(x):
                rem[removable[i]] = True
            pi = 0
            for i, c in enumerate(s):
                if rem[i]:
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