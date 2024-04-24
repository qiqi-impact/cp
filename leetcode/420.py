class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        l = string.ascii_lowercase
        h = string.ascii_uppercase
        d = string.digits
        o = '!.'

        ml = 'ab'
        mh = 'AB'
        md = '01'

        sl = set([c for c in l])
        sh = set([c for c in h])
        sd = set([c for c in d])

        which = {}
        for x in sl:
            which[x] = 0
        for x in sh:
            which[x] = 1
        for x in sd:
            which[x] = 2
        
        @cache
        def dp(di, si, last, same, valid):
            ret = inf
            if di >= 6 and valid%8 == 7:
                ret = len(s)-si
            if di == 20:
                return ret
            if si < len(s):
                ret = min(ret, 1 + dp(di, si+1, last, same, valid))
                c = s[si]
                vv = valid
                if c in which:
                    vv = valid | (1 << which[c])
                if c != last or not same:
                    ret = min(ret, dp(di+1, si+1, c, c == last, vv))
                for a, b in enumerate([ml, mh, md]):
                    for c in b:
                        if c != last or not same:
                            ret = min(ret, 1 + dp(di+1, si+1, c, c == last, valid | (1 << a)))
                for c in o:
                    if c != last or not same:
                        ret = min(ret, 1 + dp(di+1, si+1, c, c == last, valid))
            for a, b in enumerate([ml, mh, md]):
                for c in b:
                    if c != last or not same:
                        ret = min(ret, 1 + dp(di+1, si, c, c == last, valid | (1 << a)))
            for c in o:
                if c != last or not same:
                    ret = min(ret, 1 + dp(di+1, si, c, c == last, valid))
            return ret
        
        return dp(0, 0, None, False, 0)