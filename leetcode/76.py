class Solution:
    def minWindow(self, s: str, t: str) -> str:
        f = {}
        ct = 0
        for c in t:
            if c not in f:
                f[c] = 0
                ct += 1
            f[c] += 1
        
        mn = 1e9
        mni = None
        
        r = 0
        for l in range(len(s)):
            while ct > 0 and r != len(s):
                c = s[r]
                if c not in f:
                    f[c] = 0
                f[c] -= 1
                if f[c] == 0:
                    ct -= 1
                r += 1
            if ct > 0:
                break
            if r - l < mn:
                mn = r - l
                mni = l
            c = s[l]
            f[c] += 1
            if f[c] == 1:
                ct += 1
        
        if mni is None:
            return ''
        return s[mni:mni+mn]