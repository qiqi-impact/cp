class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        
        n = len(parent)
        np = parent[:]
        g = [[] for _ in range(n)]
        for i, x in enumerate(parent):
            if i != 0:
                g[x].append(i)

        lst = defaultdict(list)
        def dfs(node, p):
            v = s[node]
            if len(lst[v]):
                np[node] = lst[v][-1]
            lst[v].append(node)
            for x in g[node]:
                if x != p:
                    dfs(x, node)
            lst[v].pop()
        dfs(0, -1)

        g = [[] for _ in range(n)]
        for i, x in enumerate(np):
            if i != 0:
                g[x].append(i)

        ret = [0] * n
        def dfs2(node, p):
            ct = 1
            for x in g[node]:
                if x != p:
                    ct += dfs2(x, node)
            ret[node] = ct
            return ct
        dfs2(0, -1)
        return ret
        