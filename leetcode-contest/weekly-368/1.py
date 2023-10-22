

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        t = inf
        s = inf
        
        left = defaultdict(int)
        right = defaultdict(int)

        
        for i in range(n):
            v = nums[i]
            if v > t:
                left[i] = t
            t = min(t, v)
            
        for i in range(n-1, -1, -1):
            v = nums[i]
            if v > s:
                right[i] = s
            s = min(s, v)
        
        r = inf
        for i in range(1, n):
            if i in left and i in right:
                r = min(r, nums[i] + left[i] + right[i])
        return r if r != inf else -1