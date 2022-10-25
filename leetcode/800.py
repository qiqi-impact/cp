class Solution:
    def similarRGB(self, color: str) -> str:
        s = '0123456789abcdef'
        d = {}
        for i, c in enumerate(s):
            d[c] = i
        l = [d[x] for x in color[1:]]
        a = 16*l[0] + l[1]
        b = 16*l[2] + l[3]
        c = 16*l[4] + l[5]
        mndf = float('inf')
        best = None
        for i in range(16):
            for j in range(16):
                for k in range(16):
                    df = (17*i - a)**2 + (17*j - b)**2 + (17*k - c)**2
                    if df < mndf:
                        mndf = df
                        best = '#'+2*s[i]+2*s[j]+2*s[k]
        return best