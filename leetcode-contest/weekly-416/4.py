class Solution:
    def validSubstringCount(self, a: str, b: str) -> int:
        a = [ord(c)-97 for c in a]
        b = [ord(c)-97 for c in b]
        q = [[] for _ in range(26)]
        df = [0] * 26
        val = [inf] * 26
        for c in b:
            df[c] += 1
            val[c] = -inf
        ret = 0
        for i in range(len(a)):
            v = a[i]
            if df[v]:
                q[v].append(i)
                if len(q[v]) >= df[v]:
                    val[v] = q[v][len(q[v]) - df[v]]
            t = min(val)
            if t > -inf:
                ret += t + 1
        return ret