class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        s = set(restricted)
        g = defaultdict(list)
        for x, y in edges:
            g[x].add(y)
            g[y].add(x)
        def dfs(node, p):
            if node in s:
                return 0
            ret = 1
            for ch in g[node]:
                if ch != p:
                    ret += dfs(ch, node)
            return ret
        return dfs(0, -1)