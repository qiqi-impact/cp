class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        prime = '2357'
        MOD = int(1e9)+7
        
        if s[0] not in prime or s[-1] in prime:
            return 0
        
        block = []
        last = 0
        for i in range(1, len(s)):
            if s[i] in prime and s[i-1] not in prime:
                block.append(i - last)
                last = i
        block.append(len(s) - last)
        lb = len(block)
        
        j = 0
        sm = 0
        first = [None for _ in range(lb)]
        for i in range(lb):
            while j < lb and sm < minLength:
                sm += block[j]
                j += 1
            if sm >= minLength:
                first[i] = j
            sm -= block[i]
                
        dp = [[0 for _ in range(k+1)] for _ in range(lb+1)]
        dp[lb][0] = 1
        
        for left in range(1, k+1):
            sm = 0
            ptr = lb
            for i in range(lb-1, -1, -1):
                if first[i] is None:
                    continue
                while ptr >= first[i]:
                    sm += dp[ptr][left-1]
                    sm %= MOD
                    ptr -= 1
                dp[i][left] = sm
        return dp[0][k]
        