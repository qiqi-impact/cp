class Solution:
    def solve(self, edges):
        g = defaultdict(set)
        for x, y in edges:
            g[x].add(y)
            g[y].add(x)
            root = x

        ans = 0
        def dfs(node, p):
            nonlocal ans
            ret = 1
            best = []
            for ch in g[node]:
                if ch != p:
                    best.append(dfs(ch, node))
                if len(best) > 2:
                    best.sort(reverse=True)
                    best.pop()
            best.sort(reverse=True)
            if len(best) == 2:
                ans = max(ans, 1 + sum(best))
            elif len(best) == 1:
                ans = max(ans, 1 + best[0])
            if not best:
                best = [0]
            return 1 + best[0]
        dfs(root, -1)
        return ans