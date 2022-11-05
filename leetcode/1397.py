def lps(p):
    l1 = len(p)
    j = 0
    i = 1
    prefix = [0]
    while len(prefix) < l1:
        if p[j] == p[i]:
            prefix.append(j+1)
            i += 1
            j += 1
        else:
            if j == 0:
                prefix.append(0)
                i += 1
            if j != 0:
                j = prefix[j-1]
    return prefix

MOD = int(1e9)+7

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        evil = [ord(c)-97 for c in evil]
        def f(s):
            nonlocal evil
            LPS = lps(evil)
            
            
            le = len(evil)

            dp = [[0 for _ in range(2)] for _ in range(le)]
            dp[0][1] = 1
            
            def find_pfx_ln(pl, cc):
                while 1:
                    if evil[pl] == cc:
                        return pl+1
                    if pl == 0:
                        return 0
                    pl = LPS[pl-1]
        
            for i in range(len(s)):
                ndp = [[0 for _ in range(2)] for _ in range(le)]
                c = s[i]
                for k in range(2):
                    lmt = 25 if k == 0 else c
                    for pfxln in range(le):
                        cur = dp[pfxln][k]
                        if cur == 0:
                            continue
                        for nx in range(lmt+1):
                            npl = find_pfx_ln(pfxln, nx)
                            ltd = int(k == 1 and nx == lmt)
                            if npl != le:
                                ndp[npl][ltd] += cur
                                ndp[npl][ltd] %= MOD
                dp = ndp
            
            ret = 0
            for i in range(le):
                for j in range(2):
                    ret += dp[i][j]
                    ret %= MOD
            return ret

        s1 = [ord(c)-97 for c in s1]
        s2 = [ord(c)-97 for c in s2]
        q = f(s2)
        found = False
        for i in range(len(s1)-1, -1, -1):
            if s1[i] == 0:
                s1[i] = 25
            else:
                s1[i] -= 1
                found = True
                break
        if found:
            q -= f(s1)
        q = (q % MOD + MOD) % MOD
        return q