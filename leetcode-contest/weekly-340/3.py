class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        def can(x):
            amt = 0
            take = None
            for n in nums:
                if take is None:
                    take = n
                elif n - take <= x:
                    amt += 1
                    take = None
                    if amt >= p:
                        return True
                else:
                    take = n
            return False
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mi = (l+r)//2
            if can(mi):
                r = mi
            else:
                l = mi + 1
        return r
        