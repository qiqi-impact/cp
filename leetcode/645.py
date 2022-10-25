class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        ret = []
        for n in nums:
            if n in s:
                ret.append(n)
            s.add(n)
        N = len(nums)
        ret.append(N*(N+1)//2 - sum(nums) + ret[0])
        return ret