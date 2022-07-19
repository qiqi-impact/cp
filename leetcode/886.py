class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        a = [None] * n
        g = defaultdict(set)
        
        for x, y in dislikes:
            x -= 1
            y -= 1
            g[x].add(y)
            g[y].add(x)      
        
        def dfs(idx, val):
            if a[idx] == val:
                return True
            elif a[idx] == 1-val:
                return False
            else:
                a[idx] = val
                for other in g[idx]:
                    if not dfs(other, 1-val):
                        return False
                return True
            
        for i in range(n):
            if a[i] is None:
                if not dfs(i, 0):
                    return False
        return True