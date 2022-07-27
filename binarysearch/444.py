class Solution:
    def solve(self, s, p):
        m = {}
        values = set()
        def dfs(i, j):
            if j == len(p):
                print(m)
                return i == len(s)
            if p[j] in m:
                v = m[p[j]]
                if v == s[i:i+len(v)]:
                    return dfs(i+len(v), j+1)
                else:
                    return False
            else:
                for k in range(i+1, len(s)+1):
                    q = s[i:k]
                    if q not in values:
                        m[p[j]] = q
                        values.add(q)
                        if dfs(k, j+1):
                            return True
                        values.discard(q)
                        del m[p[j]]
            return False
        return dfs(0, 0)