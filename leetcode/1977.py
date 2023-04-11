class Solution:
    def numberOfCombinations(self, num: str) -> int:
        q = [int(x) for x in num]
        n = len(q)

        lcp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1):
                nx = 0
                if i+1 < n and j+1 < n:
                    nx = lcp[i+1][j+1]
                lcp[i][j] = nx+1 if q[i] == q[j] else 0
                
        def can(idx, ln):
            if idx+ln == n:
                return True
            if q[idx] == 0 or q[idx+ln] == 0:
                return False
            v = lcp[idx+ln][idx]
            if v >= ln:
                return True
            if q[idx+v] > q[idx+ln+v]:
                return False
            return True
            
        DP = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for idx in range(n, -1, -1):
            for ln in range(n, 0, -1):
                if idx + ln > n or q[idx] == 0:
                    DP[idx][ln] = 0
                elif idx == n or idx + ln == n:
                    DP[idx][ln] = 1
                else:
                    ret = DP[idx][ln+1]
                    if idx+2*ln <= n and can(idx, ln):
                        ret += DP[idx+ln][ln]
                    else:
                        ret += DP[idx+ln][ln+1]
                    ret %= 10**9+7
                    DP[idx][ln] = ret
        
        return DP[0][1]