class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        ret = 0
        for c in s:
            if c == 'a':
                ret += 1
            else:
                ret -= 1
        return abs(ret)