class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9+7

        @cache
        def dp(a, b):
            if a == goal:
                ret = int(b == n)
            else:
                ret = 0
                if b > k:
                    ret += (b-k) * dp(a+1, b)
                if n > b:
                    ret += (n-b) * dp(a+1, b+1)
            return ret%MOD

        return dp(0, 0)