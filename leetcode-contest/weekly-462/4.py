class Solution:
    def specialPalindrome(self, n: int) -> int:
        @cache
        def digs(idx, left, used_mid):
            if idx == 0:
                if left == 0:
                    return [[]]
                else:
                    return []
            ret = digs(idx-1, left, used_mid)[:]
            if (left >= idx) and ((not used_mid) or (idx % 2 == 0)):
                q = digs(idx-1, left - idx, used_mid or (idx % 2))
                for x in q:
                    ret.append(x + [idx])
            return ret

        @cache
        def dp(r, cl, mid, lim, dd):
            if len(r) == cl // 2:
                z = int(r + (str(mid) if mid is not None else '') + r[::-1])
                return z if z > n else inf
            d = list(dd)
            st = 0
            if lim:
                st = int(sn[len(r)])
            ret = inf
            for q in range(st, 10):
                if d[q] >= 2:
                    d[q] -= 2
                    ret = min(ret, dp(r + str(q), cl, mid, lim and q == st, tuple(d)))
                    d[q] += 2
            return ret
        
        sn = str(n)
        nl = len(sn)
        cl = nl
        while 1:
            opts = digs(9, cl, False)
            best = inf
            for l in opts:
                mid = None
                d = [0] * 10
                for x in l:
                    d[x] = x
                    if x % 2:
                        mid = x
                lim = (nl == cl)
                best = min(best, dp('', cl, mid, lim, tuple(d)))
                dp.cache_clear()
            if best != inf:
                return best
            cl += 1
                ©leetcode