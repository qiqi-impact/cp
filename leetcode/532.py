class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        ret = 0
        if k == 0:
            for x in d:
                if d[x] >= 2:
                    ret += 1
            return ret
        for x in d:
            if d[x] * d[k+x]:
                ret += 1
        return ret