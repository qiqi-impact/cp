class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        l = [int(x) for x in s]
        if max(l) > k:
            return -1
        ret = 0
        cur = 0
        for i in range(len(l)):
            nc = cur * 10 + l[i]
            if nc > k:
                ret += 1
                cur = l[i]
            else:
                cur = nc
        return ret + 1