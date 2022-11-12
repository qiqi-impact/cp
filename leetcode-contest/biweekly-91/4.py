class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        SUFFIX_TOO_LARGE = -1
        
        def can(x):
            ret = []
            mp = 0
            for i in range(1, x+1):
                app = "<" + str(i) + "/" + str(x) + ">"
                la = len(app)
                if la >= limit:
                    return SUFFIX_TOO_LARGE
                ret.append(message[mp:mp+limit-la] + app)
                mp += limit - la
                if mp >= len(message):
                    return ret
            return []
        
        l, r = 1, int(1e4)
        while l < r:
            mi = (l+r)//2
            x = can(mi)
            if x == SUFFIX_TOO_LARGE or len(x):
                r = mi
            else:
                l = mi + 1
        t = can(r)
        return t if t != SUFFIX_TOO_LARGE else []