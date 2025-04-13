MX = 10001
VAL = 1000000
comb = {}
comb[0, 0] = 1
comb[1, 0] = 1
comb[1, 1] = 1

for i in range(MX):
    comb[i, 0] = 1
    comb[i, i] = 1

def get_comb(a, b):
    r = comb.get((a, b), VAL)
    return r

for i in range(2, MX+1):
    for j in range(1, (i+1)//2+1):
        if j > 0:
            comb[i, j] = comb.get((i, j), 0) + get_comb(i-1, j-1)
        comb[i, j] = comb.get((i, j), 0) + get_comb(i-1, j)
        if comb[i, j] >= VAL:
            comb[i, j] = VAL
            break
    for j in range(i-1, (i+1)//2, -1):
        if j > 0:
            comb[i, j] = comb.get((i, j), 0) + get_comb(i-1, j-1)
        comb[i, j] = comb.get((i, j), 0) + get_comb(i-1, j)
        if comb[i, j] >= VAL:
            comb[i, j] = VAL
            break

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        ct = Counter(s)
        center = ''
        for z in ct:
            if ct[z] % 2:
                ct[z] -= 1
                center = z
        cts = [0] * 26
        for z in ct:
            cts[ord(z) - 97] = ct[z] // 2
        sm = sum(cts)

        sml = sm
        b = 1
        for q in cts:
            b *= get_comb(sml, q)
            sml -= q
            if b >= VAL:
                break
        if b < k:
            return ''

        k -= 1
        
        ret = ''
        cur = k
        for i in range(len(s) // 2):
            t = 0
            for j in range(26):
                if not cts[j]:
                    continue
                cts[j] -= 1
                sm -= 1

                sml = sm
                b = 1
                for q in cts:
                    b *= get_comb(sml, q)
                    sml -= q
                    if b >= VAL:
                        break
                
                if t + b > cur:
                    ret += chr(j + 97)
                    cur -= t
                    break
                else:
                    t += b
                    cts[j] += 1
                    sm += 1
        return ret + center + ret[::-1]
                        


        
        