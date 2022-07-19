class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)
        
        s = [ord(c)-97 for c in s]
        d = [[] for _ in range(26)]
        cum = [[0 for _ in range(26)] for _ in range(len(s)+1)]
        for i in range(len(s)):
            d[s[i]].append(i)
            for j in range(26):
                cum[i+1][j] = cum[i][j] + int(s[i] == j)
        
        ret = 0
        def dfs(a, b):
            nonlocal ret
            if a >= b:
                return
            for j in range(26):
                if 0 < cum[b+1][j] - cum[a][j] < k:
                    idx = bisect_left(d[j], a)
                    mi = d[j][idx]
                    dfs(a, mi-1)
                    dfs(mi+1, b)
                    return
            ret = max(ret, b-a+1)
        dfs(0, len(s)-1)
        return ret