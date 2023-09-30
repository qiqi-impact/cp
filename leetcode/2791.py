class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i, x in enumerate(parent):
            if i != 0:
                g[x].append((i, s[i]))
        
        d = defaultdict(int)
        
        ok = [0]
        for i in range(26):
            ok.append(1 << i)
        
        ret = 0
        bm = 0
        def dfs(node):
            nonlocal bm, ret
            for o in ok:
                ret += d[o ^ bm]
            d[bm] += 1
            for x, y in g[node]:
                bm ^= 1 << (ord(y)-97)
                dfs(x)
                bm ^= 1 << (ord(y)-97)
            
        dfs(0)
        return ret