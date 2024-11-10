class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        inc = []
        cur = -inf
        r = 0
        for x in nums:
            if x > cur:
                r += 1
            else:
                r = 1
            cur = x
            inc.append(r)

        def check(x):
            for i in range(2*x - 1, len(nums)):
                if inc[i] >= x and inc[i-x] >= x:
                    return True
            return False

        a, b = 1, len(nums)//2
        while a < b:
            mi = (a + b + 1) // 2
            if check(mi):
                a = mi
            else:
                b = mi - 1
        return a