class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        m = {}
        used = set()
        def dfs(si, pi):
            if si == len(s):
                return pi == len(pattern)
            if pi == len(pattern):
                return False
            c = pattern[pi]
            cur = ''
            for i in range(si, len(s)):
                cur += s[i]
                if cur in m:
                    if m[cur] != c:
                        continue
                    if dfs(i+1, pi+1):
                        return True
                else:
                    if c in used:
                        continue
                    else:
                        m[cur] = c
                        used.add(c)
                        if dfs(i+1, pi+1):
                            return True
                        used.discard(c)
                        del m[cur]
            return False
        return dfs(0, 0)