class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        ret = 0
        
        pf = [nums[0]]
        for i in range(1, len(nums)):
            pf.append(pf[-1] + nums[i])
            
        left = defaultdict(int, Counter(pf))
        right = defaultdict(int)
        delta = 0
            
        if pf[-1]%2 == 0:
            ret += left[pf[-1]//2]
            if pf[-1] == 0:
                ret -= 1
        
        for i in range(len(nums)-1, -1, -1):
            v = nums[i]
            p = pf[i]
            df = k - v
            ovr = pf[-1] + df
            delta += df - ((k - nums[i+1]) if i < len(nums)-1 else 0)
            left[p] -= 1
            right[p+df-delta] += 1
            
            if ovr%2 == 0:
                cur = left[ovr//2] + right[ovr//2 - delta]
                if ovr == 0:
                    cur -= 1
                ret = max(ret, cur)
        return ret
        