class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = [set() for _ in range(n)]
        
        for x, y in edges:
            g[x].add(y)
            g[y].add(x)
        
        def dfs(i, p):
            r = nums[i]
            for x in g[i]:
                if x != p:
                    r += dfs(x, i)
            return r
        s = dfs(0, -1)
        
        def can(x):
            def rem(idx, p):
                amt = nums[idx]
                for other in g[idx]:
                    if other != p:
                        amt += rem(other, idx)
                return amt if amt != x else 0
            return rem(0, -1) == 0

        for q in range(1, 1+s):
            if s % q == 0:
                if can(q):
                    return s // q - 1