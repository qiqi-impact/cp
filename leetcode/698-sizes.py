# this one is really fast

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s%k != 0:
            return False
        tgt = s//k
        
        for n in nums:
            if n > tgt:
                return False
        
        ret = False
        nums.sort(reverse=True)
        
        @cache
        def divide(idx, sizes):
            nonlocal ret, tgt, k
            if idx == len(nums):
                ret = True
                return 1
            w = nums[idx]
            ss = list(sizes)
            if len(ss) < k and divide(idx+1, tuple(sorted([w] + ss))):
                return 1
            for i in range(len(ss)):
                if sizes[i] + w <= tgt:
                    ss[i] += w
                    if divide(idx+1, (tuple(sorted(ss)))):
                        return 1
                    ss[i] -= w
                else:
                    break
        divide(0, tuple())
        return ret