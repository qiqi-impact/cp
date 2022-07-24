class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        assignment = [None] * len(graph)
        
        def dfs(idx, a):
            if assignment[idx] == a:
                return True
            if assignment[idx] == 1-a:
                return False
            assignment[idx] = a
            for x in graph[idx]:
                if not dfs(x, 1-a):
                    return False
            return True
        
        for i in range(len(graph)):
            if assignment[i] is None:
                if not dfs(i, 0):
                    return False
        return True