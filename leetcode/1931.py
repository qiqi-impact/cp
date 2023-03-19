class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9+7
        l = []
        cur = []
        def dfs(idx):
            if idx == m:
                l.append(tuple(cur))
                return
            for i in range(3):
                if not cur or cur[-1] != i:
                    cur.append(i)
                    dfs(idx+1)
                    cur.pop()
        dfs(0)
        d = defaultdict(int)
        for x in l:
            d[x] = 1
        for i in range(n-1):
            nd = defaultdict(int)
            for x in l:
                for k in d:
                    fail = False
                    for j in range(m):
                        if k[j] == x[j]:
                            fail = True
                            break
                    if not fail:
                        nd[x] += d[k]
                        nd[x] %= MOD
            d = nd
        return sum(d.values()) % MOD