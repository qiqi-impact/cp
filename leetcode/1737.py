class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        af = [0] * 26
        bf = [0] * 26
        
        for c in a:
            af[ord(c) - 97] += 1
        for c in b:
            bf[ord(c) - 97] += 1
            
        pa, pb = [0]*26, [0]*26
        pa[0] = af[0]
        pb[0] = bf[0]
        for i in range(1, len(af)):
            pa[i] = pa[i-1] + af[i]
            pb[i] = pb[i-1] + bf[i]
        
        sa, sb = [0]*26, [0]*26
        sa[-1] = af[-1]
        sb[-1] = bf[-1]
        for i in range(len(af)-2, -1, -1):
            sa[i] = sa[i+1] + af[i]
            sb[i] = sb[i+1] + bf[i]
        
        ret = 1e18
        for i in range(26):
            ret = min(ret, len(a) - af[i] + len(b) - bf[i])
            if i != 25:
                ret = min(ret, sa[i+1] + pb[i], sb[i+1] + pa[i])
        
        return ret