class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        g = defaultdict(set)
        for i, x in enumerate(edges):
            if x != -1:
                g[i].add(x)
        d = {}
        lc = -1
        done = set()
        def dfs(node, depth):
            nonlocal lc, done
            if node in done:
                return
            if node in d:
                lc = max(lc, depth - d[node])
                return
            d[node] = depth
            for ch in g[node]:
                dfs(ch, depth+1)
        
        for i in range(len(edges)):
            d = {}
            dfs(i, 0)
            done |= set(d.keys())
            
        return lc