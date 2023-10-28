class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[y].append(x)

        @cache
        def dfs(node):
            ret = []
            for x in g[node]:
                ret.append(x)
                ret += dfs(x)
            return sorted(set(ret))

        return [dfs(x) for x in range(n)]