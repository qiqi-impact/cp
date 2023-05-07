class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        cost = [None] + cost
        ret = 0
        
        def dfs(idx):
            nonlocal ret
            if 2*idx > n:
                return cost[idx]
            a = dfs(2*idx)
            b = dfs(2*idx+1)
            ret += max(a,b) - min(a,b)
            return cost[idx] + max(a,b)
        
        dfs(1)
        return ret