class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9+7
        arr.sort()
        m = {}
        dp = [1] * len(arr)
        for i, e in enumerate(arr):
            m[e] = i
            for j in range(i):
                x = arr[j]
                if e % x != 0:
                    continue
                y = e // x
                if y in m:
                    k = m[y]
                    dp[i] += dp[j] * dp[k]
                    dp[i] %= MOD
        return sum(dp)%MOD