class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def f(ss):
            if not ss: return True
            p = 0
            rt = 0
            for i in range(len(s)):
                if s[i] == ss[p]:
                    p += 1
                    if p == len(ss):
                        p = 0
                        rt += 1
                        if rt == k:
                            return True
            return False
        
        ret = ''
        
        ct = Counter(s)
        opts = []
        for i in range(25, -1, -1):
            c = chr(ord('a')+i)
            if ct[c] >= k:
                opts.append(c)
        
        def g(ss):
            nonlocal ret
            if f(ss):
                if len(ss) > len(ret):
                    ret = ss
                if len(ss) < 7:
                    for c in opts:
                        g(ss + c)
        
        g('')
        return ret