class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        
        def can(x):
            opts = set()
            f = {}
            w = 2*x+1
            for i in range(w):
                a = i%n
                f[nums[a]] = f.get(nums[a], 0) + 1
                opts.add(nums[a])
            for i in range(w, n+w):
                a, b = i%n, (i-w)%n
                f[nums[a]] = f.get(nums[a], 0) + 1
                f[nums[b]] = f.get(nums[b], 0) - 1
                if not f[nums[b]]:
                    del f[nums[b]]
                    opts.discard(nums[b])
            return len(opts)
        
        l, r = 0, len(nums)-1
        while l < r:
            mi = (l+r)//2
            if can(mi):
                r = mi
            else:
                l = mi+1
        return r