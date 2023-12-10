class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        def can(x):
            ret = []
            mp = 0
            for i in range(1, x+1):
                app = "<" + str(i) + "/" + str(x) + ">"
                la = len(app)
                if la >= limit:
                    break
                ret.append(message[mp:mp+limit-la] + app)
                mp += limit - la
                if mp >= len(message):
                    return ret
            return []
        
        for p in range(4):
            l, r = 10**p, 10**(p+1)-1
            while l < r:
                mi = (l+r)//2
                x = can(mi)
                if x:
                    r = mi
                else:
                    l = mi + 1
            t = can(r)
            if t:
                return t
        return []