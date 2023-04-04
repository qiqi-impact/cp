class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        pf = [-1] * len(s)
        sf = [len(t)] * len(s)
        
        pt = 0
        for i in range(len(s)):
            if s[i] == t[pt]:
                pt += 1
                if pt == len(t):
                    return 0
            pf[i] = pt
        ret = len(t) - pt
            
        pt = len(t)-1
        for i in range(len(s)-1, -1, -1):
            if s[i] == t[pt]:
                pt -= 1
            sf[i] = pt
        ret = min(ret, pt + 1)
        
        for i in range(len(s)-1):
            ret = min(ret, sf[i+1] - pf[i] + 1)
        return ret