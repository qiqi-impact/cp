class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        N = len(vals)
        g = [[] for _ in range(N)]
        
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        ss = list(range(N))
        ss.sort(key=lambda x:-vals[x])
        
        ct = [0] * N
        sums =vals[:]
        ret = max(vals)
        for idx in ss:
            if vals[idx] <= 0: break
            for ch in g[idx]:
                if ct[ch] < k:
                    sums[ch] += vals[idx]
                    ct[ch] += 1
                    ret = max(ret, sums[ch])
        return ret