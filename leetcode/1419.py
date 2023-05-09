class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        l = ['croak'.find(c) for c in croakOfFrogs]
        ct = [0,0,0,0]
        ret = 0
        for x in l:
            if x > 0:
                ct[x-1] -= 1
            if x < 4:
                ct[x] += 1
            if min(ct) == -1:
                return -1
            ret = max(ret, sum(ct))
        if sum(ct) != 0:
            return -1
        return ret