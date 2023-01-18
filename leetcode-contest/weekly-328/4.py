class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        MIN = float('-inf')
        
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        ret = 0
        def dfs(idx, p):
            nonlocal ret
            ml, mnl = 0, -inf
            has_child = False
            for ch in g[idx]:
                if ch != p:
                    l, nl = dfs(ch, idx)
                    ret = max(ret, l + mnl + price[idx])
                    ret = max(ret, nl + ml + price[idx])
                    ml = max(l, ml)
                    mnl = max(nl, mnl, 0)
                    has_child = True
            max_path_to_leaf = price[idx] + ml
            max_path_to_non_leaf = (price[idx] + max(0, mnl)) if has_child else MIN
            if len(g[idx]) == 1:
                ret = max(ret, max_path_to_non_leaf)
            ret = max(ret, max_path_to_leaf - price[idx])
            return [max_path_to_leaf, max_path_to_non_leaf]
        
        dfs(0, -1)
        return ret