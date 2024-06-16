MOD = 10**9+7
fac = [1]
inv = [1]
for i in range(1, 10**5+1):
    fac.append(fac[-1] * i % MOD)
    inv.append(pow(fac[-1], -1, MOD))

class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        n = len(prevRoom)
        g = [[] for _ in range(n)]
        for i, x in enumerate(prevRoom):
            if i != 0:
                g[x].append(i)

        def dfs(node):
            l = []
            q = 1
            sm = 0
            for ch in g[node]:
                l.append(dfs(ch))
                q *= l[-1][0]
                q %= MOD
                sm += l[-1][1]
            ret = fac[sm]
            for x in l:
                ret *= inv[x[1]]
                ret %= MOD
            return (ret * q % MOD, sm+1)
        return dfs(0)[0]
