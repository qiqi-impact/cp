class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        d = defaultdict(int)
        for x, y in pairs:
            g[x].append(y)
            d[x] += 1
            d[y] -= 1
            src = x
        for k in d:
            if d[k] == 1:
                src = k
                break
        ret = []
        def dfs(node):
            while g[node]:
                nx = g[node].pop()
                dfs(nx)
            ret.append(node)
        dfs(src)
        return list(pairwise(ret[::-1]))