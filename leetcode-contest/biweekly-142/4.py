MOD = 10**9+7

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        if k > len(word):
            return 0
        if k == len(word):
            return 1
        runs = []
        run = 0
        lst = None
        for x in word:
            if x == lst:
                run += 1
            else:
                if run:
                    runs.append(run)
                run = 1
            lst = x
        runs.append(run)
        ct = Counter(runs)

        l = list(ct.items())
        tot = 1
        for x, y in l:
            tot *= x**y
        k -= len(runs)

        if k <= 0:
            return tot % MOD
            
        dp = [0] * k
        dp[0] = 1

        for x, y in l:
            x -= 1
            for _ in range(y):
                ls = [0] * k
                for i in range(k):
                    v = dp[i]
                    ls[i] += v
                    if i+x+1 < k: ls[i+x+1] -= v
                ndp = [0] * k
                cur = 0
                for i in range(k):
                    cur += ls[i]
                    ndp[i] += cur
                    ndp[i] %= MOD
                dp = ndp
                # print(dp, ls)
        tot -= sum(dp)
        tot %= MOD
        return tot
                
        

        