class Solution:
    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        sums = [0] * n
        g = [[] for _ in range(n)]
        
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        def get_sums(node, p):
            ret = values[node]
            for o in g[node]:
                if o != p:
                    ret += get_sums(o, node)
            sums[node] = ret
            return ret
        get_sums(0, -1)
        
        trie = {}
        ret = 0
        
        BITS = 63
        
        def ins(val):
            # print(val)
            cur = trie
            for i in range(BITS, -1, -1):
                k = 1 & (val >> i)
                if k not in cur:
                    cur[k] = {}
                cur = cur[k]
        
        def find_max_xor(val):
            nonlocal ret
            cur = trie
            best = 0
            if trie:
                for i in range(BITS, -1, -1):
                    k = 1 & (val >> i)
                    if 1-k in cur:
                        best ^= (1 << i)
                        cur = cur[1-k]
                    else:
                        cur = cur[k]
            ret = max(ret, best)
        
        def dfs(node, p):
            find_max_xor(sums[node])
            for ch in g[node]:
                if ch != p:
                    dfs(ch, node)
            ins(sums[node])
        dfs(0, -1)
        
        # print(trie)
        return ret
            