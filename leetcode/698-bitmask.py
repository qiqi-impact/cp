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
        N = len(nums)
        
        opts = []
        two = set()
        
        FULL = (1 << N) - 1
        
        for b in range(1 << N):
            sm = 0
            for i in range(N):
                if b & (1 << i):
                    sm += nums[i]
            if sm == tgt:
                opts.append(b)
                
        @cache
        def dfs(idx, bm):
            if bm == FULL:
                return True
            if idx == len(opts):
                return False
            if dfs(idx+1, bm):
                return True
            if opts[idx] & bm == 0:
                if dfs(idx+1, opts[idx] | bm):
                    return True
            return False
        
        return dfs(0, 0)