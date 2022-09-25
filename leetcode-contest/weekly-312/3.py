class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        l, r = [0] * n, [0] * n
        l[0] = r[-1] = 1
        
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                l[i] = l[i-1] + 1
            else:
                l[i] = 1
        
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                r[i] = r[i+1] + 1
            else:
                r[i] = 1
                
        ret = []
        for i in range(k, n-k):
            if l[i-1] >= k and r[i+1] >= k:
                ret.append(i)
        return ret
        