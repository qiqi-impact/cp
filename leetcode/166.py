class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n == 0:
            return "0"
        
        nn = n < 0
        dd = d < 0
        
        neg = nn ^ dd
        
        n = abs(n)
        d = abs(d)
        
        whole = n // d
        n %= d
        if n == 0:
            return ('-' if neg else '') + str(whole)
        ret = []
        seen = {}
        cur = 0
        rpt = 0
        while 1:
            n *= 10
            if n in seen:
                rpt = cur - seen[n]
                break
            seen[n] = cur
            amt = n // d
            ret.append(amt)
            n %= d
            if n == 0:
                break
            cur += 1
        ans = ('-' if neg else '') + str(whole) + '.'
        for i in range(len(ret)-rpt):
            ans += str(ret[i])
        if rpt:
            ans += '('
            for i in range(len(ret)-rpt, len(ret)):
                ans += str(ret[i])
            ans += ')'
        return ans