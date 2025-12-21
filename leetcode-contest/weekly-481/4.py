class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        G = 21
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        ret = 0
        def dfs(idx, p):
            nonlocal ret
            ans = [[0,0] for _ in range(G)]
            for ch in g[idx]:
                if ch != p:
                    a = dfs(ch, idx)
                    for i in range(G):
                        pc, ps = ans[i]
                        cc, cs = a[i]
                        ret += 2 * pc * cc + pc * cs + cc * ps
                        ans[i][0] += a[i][0]
                        ans[i][1] += a[i][1]
            v = group[idx]
            ret += ans[v][0] + ans[v][1]
            for i in range(G):
                ans[i][1] += ans[i][0]
            ans[v][0] += 1
            # print(idx, ans, ret)
            return ans
        dfs(0, -1)
        return ret