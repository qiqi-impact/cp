class Solution:
    def maxJump(self, stones: List[int]) -> int:
        N = len(stones)
        def can(x):
            vis = [0] * N
            idx = 0
            while idx != N-1:
                idx = bisect.bisect(stones, stones[idx] + x) - 1
                vis[idx] = 1
            cur = stones[-1]
            # print(x, vis)
            for i in range(N-1, -1, -1):
                if not vis[i]:
                    diff = cur - stones[i]
                    if diff > x:
                        return False
                    cur = stones[i]
            return True
        
        l = 0
        for i in range(N-1):
            l = max(stones[i+1] - stones[i], l)
        r = stones[-1] - stones[0]
        while l < r:
            mi = (l+r)//2
            if can(mi):
                r = mi
            else:
                l = mi + 1
        return r
                
            