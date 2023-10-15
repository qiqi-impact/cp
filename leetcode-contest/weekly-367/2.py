class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        for l in range(1, 1+len(s)):
            found = False
            t = None
            for i in range(len(s) - l + 1):
                ss = s[i:i+l]
                ct = ss.count('1')
                if ct == k:
                    found = True
                    if t is None or t > ss:
                        t = ss
            if found:
                return t                
        return ''