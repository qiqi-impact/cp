class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = sorted(set(nums))
        mx = 1
        j = 0
        for i in range(len(l)):
            while j < len(l) and l[j] - l[i] <= len(nums)-1:
                j += 1
            mx = max(mx, j - i)
        return len(nums) - mx