class Solution:
    def minimumDeletions(self, word: str, e: int) -> int:
        ct = Counter(word)
        f = defaultdict(int)
        mx = 0
        for k in ct:
            f[ct[k]] += 1
            mx = max(mx, ct[k])
        
        # print(f)
        pf = [0] 
        for i in range(1, mx+1):
            pf.append(pf[-1] + f[i] * i)
        # print(pf)
            
        ret = inf
        q = 0
        cot = 0
        for i in range(mx, 0, -1):
            # print(i, q, pf[max(0, i-e-1)])
            ret = min(ret, q + pf[max(0, i-e-1)])
            cot += f[i]
            q += cot
        return ret