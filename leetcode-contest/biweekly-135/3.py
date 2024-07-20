class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        ls = [0] * (k+2)
        n = len(nums)
        for i in range(n//2):
            v = abs(nums[i] - nums[n-1-i])
            a, b = nums[i], nums[n-1-i]
            if a > b:
                a, b = b, a
                
            ls[v] -= 1
            ls[v + 1] += 1
            
            ls[0] += 1
            t = max(a, b, k - a, k - b) + 1
            ls[t] += 1
            
        mn = inf
        cur = 0
        for i in range(k+1):
            cur += ls[i]
            mn = min(mn, cur)
        return mn