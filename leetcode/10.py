class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pp = []
        for c in p:
            if c == '*':
                pp[-1] += c
            else:
                pp.append(c)
                
        tail_star = len(pp)
        while tail_star > 0 and len(pp[tail_star-1]) == 2:
            tail_star -= 1
        
        @cache
        def match(i, j):  
            if j == len(pp):
                return i == len(s)

            if i == len(s):
                return j >= tail_star
            
            if len(pp[j]) == 2:
                ret = match(i, j+1)
                if pp[j][0] in ['.', s[i]]:
                    ret = ret or match(i+1, j)
            else:
                ret = False
                if pp[j][0] in ['.', s[i]]:
                    ret = match(i+1, j+1)

            return ret
        
        return match(0, 0)