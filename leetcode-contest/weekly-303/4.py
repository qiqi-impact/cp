class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        sn = set(nums)
        l = [x.bit_count() for x in sn]
        l.sort()
        ret = 0
        for i in range(len(l)):
            ret += len(l) - bisect.bisect_left(l, k-l[i])
        return ret