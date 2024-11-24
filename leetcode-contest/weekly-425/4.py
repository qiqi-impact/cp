
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        g = [{} for _ in range(n)]
        for x, y, w in edges:
            g[x][y] = g[y][x] = w
        
        def dfs(idx, p):
            ret = [0, 0]
            h = []
            for ch in g[idx]:
                if ch != p:
                    [a, b] = dfs(ch, idx)
                    heapq.heappush(h, (a-b, a, b))
            take = 0
            take_k = 0
            leave_k = 0
            leave = 0
            ct = 0
            while h:
                _, a, b = heapq.heappop(h)
                ct += 1
                if ct <= k - 1:
                    take += b
                elif ct == k:
                    take_k = b
                    leave_k = a
                else:
                    leave += a
            v = take + take_k + leave
            w = take + leave_k + leave + (g[p][idx] if p != -1 else 0)
            r = [v, max(v, w)]
            return r
        return dfs(0, -1)[1]
                