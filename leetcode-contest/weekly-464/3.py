class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ct = defaultdict(int)
        ret = 0
        run = 0
        lstab = {0:-1}
        lstbc = {0:-1}
        lstca = {0:-1}
        lstabc = {(0,0,0):-1}
        for i in range(n):
            c = s[i]
            if i > 0 and c == s[i-1]:
                run += 1
            else:
                run = 1
            ret = max(ret, run)
            ct[c] += 1
            # print(ct, lstabc)
            ab = ct['a'] - ct['b']
            bc = ct['b'] - ct['c']
            ca = ct['c'] - ct['a']
            if (ab, bc, ca) in lstabc:
                ret = max(ret, i - lstabc[ab, bc, ca])
            else:
                lstabc[ab, bc, ca] = i
            if ab not in lstab:
                lstab[ab] = i
            if bc not in lstbc:
                lstbc[bc] = i
            if ca not in lstca:
                lstca[ca] = i
            if c == 'a':
                lstbc = {bc: i}
            elif c == 'b':
                lstca = {ca: i}
            else:
                lstab = {ab: i}
            if ab in lstab:
                ret = max(ret, i - lstab[ab])
            if bc in lstbc:
                ret = max(ret, i - lstbc[bc])
            if ca in lstca:
                ret = max(ret, i - lstca[ca])
        return ret
            
            
            
            
            