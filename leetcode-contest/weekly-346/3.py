class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can(x):
            s = str(x*x)
            
            @cache
            def dfs(i, s, x):
                if i == len(s):
                    return set([0])
                cur = 0
                ret = set()
                x = int(s)
                for j in range(i, len(s)):
                    cur = cur * 10 + int(s[j])
                    if cur > x:
                        break
                    v = dfs(j+1, s, x)
                    for t in v:
                        if cur + t <= x:
                            ret.add(cur + t)
                return ret
            return x in dfs(0, s, x)
                    
        
        return sum([x*x for x in range(1, n+1) if can(x)])