class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        
        g = [list() for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        visit = [list() for _ in range(n)]
        
        x = [None] * n
        vi = 0
        def fill_xor(idx, p):
            nonlocal vi
            visit[idx].append(vi)
            ret = nums[idx]
            for o in g[idx]:
                if o != p:
                    vi += 1
                    ret ^= fill_xor(o, idx)
                    vi += 1
            x[idx] = ret
            visit[idx].append(vi)
            return ret
        
        fill_xor(0, -1)
        ret = float('inf')
        for i in range(1, n):
            for j in range(1, n):
                if i != j:
                    opts = None
                    if visit[i][0] <= visit[j][0] and visit[j][1] <= visit[i][1]:
                        opts = [x[0] ^ x[i], x[i] ^ x[j], x[j]]
                    elif visit[i][1] < visit[j][0]:
                        opts = [x[0] ^ x[i] ^ x[j], x[i], x[j]]
                    if opts:
                        ret = min(ret, max(opts) - min(opts))
        return ret
                    