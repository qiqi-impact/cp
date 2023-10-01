class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        dq = set()
        for i in range(n):
            for j in range(n):
                if i != j and words[i].find(words[j]) != -1:
                    dq.add(j)
        words = [words[i] for i in range(n) if i not in dq]
        n = len(words)

        def work(s, t, a):
            for i in range(a, len(s)):
                if s[i] != t[i-a]:
                    return False
            return True
        
        pfx = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            s = words[i]
            for j in range(n):
                t = words[j]
                for k in range(1, len(s)+1):
                    if work(s, t, k):
                        pfx[i][j] = k
                        break
        @cache
        def dfs(idx, bm, last):
            if idx == n:
                return len(words[last]), -1
            ret = (inf, None)
            for i in range(n):
                if bm & (1 << i) == 0:
                    s, _ = dfs(idx+1, bm ^ (1 << i), i)
                    p = 0
                    if last is not None:
                        p = pfx[last][i]
                    ret = min(ret, (s + p, i))
            return ret

        ret = ''
        bm = 0
        last = None
        for i in range(n):
            x, y = dfs(i, bm, last)
            if last is None:
                ret += words[y]
            else:
                ret += words[y][(len(words[last]) - pfx[last][y]):]
            bm ^= 1 << y
            last = y
        return ret