class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        n = len(nums)
        g = [[] for _ in range(n)]
        
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        @cache
        def dfs(node, p, t):
            cv = nums[node]
            if t: cv ^= k
            best = -inf
            
            l = []
            sm = 0
            for o in g[node]:
                if o != p:
                    a, b = dfs(o, node, False), dfs(o, node, True)
                    l.append(b - a)
                    sm += a
            l.sort(reverse=True)
            
            best = cv + sm
            for i in range(len(l)):
                cv ^= k
                sm += l[i]
                best = max(best, cv + sm)
            return best
        
        return dfs(0, -1, 0)