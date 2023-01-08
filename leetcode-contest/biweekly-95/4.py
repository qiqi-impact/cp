class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        def can(x):
            kk = k
            acc = defaultdict(int)
            cur = 0
            for i in range(1, len(pf)-1):
                cur += acc[i]
                df = x - pf[i] - cur
                if df > 0:
                    if df > kk:
                        return False
                    kk -= df
                    cur += df
                    acc[i + 2 * r + 1] -= df
            return True
        
        n = len(stations)
        acc = [0] * (n+1)
        for i in range(n):
            acc[max(0, i - r)] += stations[i]
            acc[min(n, i + r + 1)] -= stations[i]
        pf = [0]
        cur = 0
        for c in acc:
            cur += c
            pf.append(cur)
            
        a, b = 0, 10**18
        while a < b:
            mi = (a+b+1)//2
            if can(mi):
                a = mi
            else:
                b = mi - 1
        return a