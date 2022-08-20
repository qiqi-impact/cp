class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        sz = False
        ret = 0
        cur = 0
        for i, c in enumerate(s):
            if c == '0':
                sz = True
                lz = True
                cur += 1
            elif sz:
                cur += int(not lz)
                ret = max(ret, cur)
                lz = False
        return ret