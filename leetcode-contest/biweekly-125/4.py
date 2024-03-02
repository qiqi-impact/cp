class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        n = len(nums)
        g = [[] for _ in range(n)]
        
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        def dfs(node, p, t):
            cv = nums[node]
            if t: cv ^= k
            eo = [-inf, -inf]
            
            l = []
            sm = 0
            
            for o in g[node]:
                if o != p:
                    a, b = dfs(o, node, False), dfs(o, node, True)
                    l.append(b - a)
                    sm += a
            l.sort(reverse=True)
            
            eo[0] = cv + sm
            for i in range(len(l)):
                cv ^= k
                sm += l[i]
                eo[(i+1)%2] = max(eo[(i+1)%2], cv + sm)
            return max(eo)
        
        return dfs(0, -1, 0)