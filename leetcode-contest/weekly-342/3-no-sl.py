class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ct = [0] * 101
        ret = []
        
        def find_xth():
            cur = 0
            for i in range(101):
                cur += ct[i]
                if cur >= x:
                    return min(0, i-50)
        
        for i in range(k):
            ct[nums[i]+50] += 1
        ret.append(find_xth())
        for i in range(k, len(nums)):
            ct[nums[i]+50] += 1
            ct[nums[i-k]+50] -= 1
            ret.append(find_xth())
        return ret