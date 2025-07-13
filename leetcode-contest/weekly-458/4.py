class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        g = [set() for _ in range(n)]
        c = defaultdict(list)
        for i in range(n):
            c[label[i]].append(i)
        for x, y in edges:
            g[x].add(y)
            g[y].add(x)
        ret = 1

        FULL = (1 << n) - 1
        
        @cache
        def dp(bm, a, b):
            if a > b:
                return dp(bm, b, a)
            r = 0
            for k in c:
                for xi in range(len(c[k])):
                    if bm & (1 << c[k][xi]):
                        for xj in range(xi+1, len(c[k])):
                            i, j = c[k][xi], c[k][xj]
                            if bm & (1 << j):
                                if (i in g[a] and j in g[b]) or (i in g[b] and j in g[a]):
                                    r = max(r, 2 + dp(bm ^ (1 << i) ^ (1 << j), min(i, j), max(i, j)))
            return r

        for i in range(n):
            ret = max(ret, 1 + dp(FULL ^ (1 << i), i, i))

        for i in range(n):
            for j in range(i+1, n):
                if j in g[i] and label[i] == label[j]:
                    ret = max(ret, 2 + dp(FULL ^ (1 << i) ^ (1 << j), i, j))

        return ret©leetcode