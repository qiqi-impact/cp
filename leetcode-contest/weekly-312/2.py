class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = 1
        cur = None
        ln = 0
        mv = 0
        for n in nums:
            if n != cur:
                ln = 1
            else:
                ln += 1
            cur = n
            
            if n > mv:
                mx = 1
            elif n == mv:
                mx = max(mx, ln)
            mv = max(mv, n)
            
        return mx
                