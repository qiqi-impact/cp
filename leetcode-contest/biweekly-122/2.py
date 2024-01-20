class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        t = []
        lst = None
        for x in nums:
            if x.bit_count() != lst:
                lst = x.bit_count()
                t.append([])
            t[-1].append(x)
            
        for l in t:
            l.sort()
        
        q = []
        for l in t:
            for x in l:
                q.append(x)
        
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != q[i]:
                return False
        return True