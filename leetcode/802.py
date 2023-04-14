class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        vis = [0] * n
        safe = [True] * n
        def dfs(node):
            vis[node] = 1
            for nei in graph[node]:
                if vis[nei] == 1:
                    safe[node] = False
                    continue
                elif vis[nei] == 0:
                    dfs(nei)
                if not safe[nei]:
                    safe[node] = False
            vis[node] = -1
        for i in range(n):
            if vis[i] == 0:
                dfs(i)
        return [i for i in range(n) if safe[i]]