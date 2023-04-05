class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def can(x):
            l = nums[:]
            for i in range(len(nums)-1, 0, -1):
                if l[i] > x:
                    df = l[i] - x
                    l[i] = x
                    l[i-1] += df
            if l[0] > x:
                return False
            return True
        a, b = 0, max(nums)
        while a < b:
            mi = (a+b)//2
            if can(mi):
                b = mi
            else:
                a = mi + 1
        return b