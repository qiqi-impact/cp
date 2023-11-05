class MaxBIT:
    def __init__(self, n):
        self.n = n
        self.arr = Counter()
    def get(self, i):
        ans = 0
        i += 1
        while i > 0:
            ans = max(ans, self.arr[i])
            i &= i - 1
        return ans
    def set(self, i, x):
        i += 1
        while i <= self.n:
            self.arr[i] = max(self.arr[i], x)
            i += i & -i

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        if all(x < 0 for x in nums):
            return max(nums)
        nums1 = [(x-i+len(nums), x) for i, x in enumerate(nums) if x >= 0]
        bit = MaxBIT(1 + max(a for a, x in nums1))
        ans = 0
        for i, x in nums1:
            best = bit.get(i) + x
            bit.set(i, best)
            ans = max(ans, best)
        return ans

#-------------

class FenwickTree:
    def __init__(self, n):
        self.bit = [0] * n

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] = max(self.bit[idx], x)
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x = max(x, self.bit[end - 1])
            end &= end - 1
        return x

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        order = sorted(range(n), key = lambda x: nums[x] - x)
        
        out = max(nums)
        
        seg = FenwickTree(n + 1)
        
        for i in order:
            best = seg.query(i + 1)
            best += nums[i]
            
            out = max(best, out)
            seg.update(i, best)
            
        return out