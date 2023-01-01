class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] < nums[-1]:
            rot = 0
        else:
            l, r = 0, len(nums)-1
            while l < r-1:
                mi = (l+r)//2
                a, b = nums[l], nums[mi]
                if a < b:
                    l = mi
                else:
                    r = mi
            if l == r:
                rot = l
            elif l == r - 1:
                rot = l if nums[l] < nums[r] else r
        
        def get_val(idx):
            return nums[(idx + rot)%len(nums)]
        
        l, r = 0, len(nums)-1
        while l <= r:
            mi = (l+r)//2
            v = get_val(mi)
            if v == target:
                return (mi + rot)%len(nums)
            elif v < target:
                l = mi + 1
            else:
                r = mi - 1
        return -1