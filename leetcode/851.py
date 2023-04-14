class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        ret = list(range(n))
        g = [[] for _ in range(n)]
        ind = [0] * n
        for x, y in richer:
            g[x].append(y)
            ind[y] += 1
        q = deque()
        for i in range(n):
            if ind[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            for nei in g[cur]:
                if quiet[ret[nei]] > quiet[ret[cur]]:
                    ret[nei] = ret[cur]
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)
        return ret