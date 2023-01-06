class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        ct = Counter(nums)
        ret = []
        for n in nums:
            if ct[n] == 1 and ct[n-1] == 0 and ct[n+1] == 0:
                ret.append(n)
        return ret