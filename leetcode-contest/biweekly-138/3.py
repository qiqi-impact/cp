class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        d = (n+1)//2
        ret = 0
        seen = set()
        for i in range(1, 10**d):
            if i%10 == 0:
                continue
            s = str(i).zfill(d)
            if n%2:
                s = s[::-1]+s[1:]
            else:
                s = s[::-1]+s
            if int(s)%k == 0:
                ss = ''.join(sorted(s))
                if ss in seen:
                    continue
                seen.add(ss)
                ct = Counter(s)
                v = list(ct.values())
                sm = n
                cur = 1
                for x in v:
                    cur *= math.comb(sm, x)
                    sm -= x
                if '0' in ct:
                    ct['0'] -= 1
                    v = list(ct.values())
                    sm = n-1
                    t = 1
                    for x in v:
                        t *= math.comb(sm, x)
                        sm -= x
                    cur -= t
                ret += cur
        return ret
