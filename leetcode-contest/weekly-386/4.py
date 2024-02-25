class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        ok = False
        
        n, m = len(nums), len(changeIndices)
        
        def can(x):
            mk = [0] * n
            use = [0] * x
            op = 0
            for i in range(x):
                v = changeIndices[i]-1
                if not mk[v] and nums[v]:
                    mk[v] = 1
                    use[i] = 1
                else:
                    op += 1
            h = []
            ct = 0
            for i in range(x-1, -1, -1):
                v = changeIndices[i]-1
                if use[i]:
                    heapq.heappush(h, (nums[v], i))
                    ct -= 1
                    if ct < 0:
                        ct += 2
                        a, b = heapq.heappop(h)
                        use[b] = 0
                        mk[changeIndices[b]-1] = 0
                        op += 1
                else:
                    ct += 1
                
            op -= n
            for i in range(n):
                if not mk[i]:
                    op -= nums[i]
            return op >= 0
                    
        l, r = 1, m+1
        while l < r:
            mi = (l+r)//2
            if can(mi):
                ok = True
                r = mi
            else:
                l = mi + 1
        if ok:
            return r
        return -1