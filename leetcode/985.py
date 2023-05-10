class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ret = 0
        for x in nums:
            if x%2 == 0:
                ret += x
        ans = []
        for x, y in queries:
            if nums[y]%2==0:
                ret -= nums[y]
            nums[y] += x
            if nums[y]%2==0:
                ret += nums[y]
            ans.append(ret)
        return ans