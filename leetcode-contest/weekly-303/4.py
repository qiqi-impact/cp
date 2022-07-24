class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        sn = set(nums)
        def sbit(k):
            ret = 0
            while k:
                if k%2:
                    ret += 1
                k//=2
            return ret
        l = [sbit(x) for x in sn]
        l.sort()
        ret = 0
        for i in range(len(l)):
            ret += len(l) - bisect.bisect_left(l, k-l[i])
        return ret