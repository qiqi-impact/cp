class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        @cache
        def dp(a, b, c, lst):
            if lst == 0:
                if b == 0:
                    return 0
                return 1 + dp(a, b-1, c, 1)
            elif lst == 1:
                ret = 0
                if a > 0:
                    ret = max(ret, 1 + dp(a-1, b, c, 0))
                if c > 0:
                    ret = max(ret, 1 + dp(a, b, c-1, 2))
                return ret
            else:
                ret = 0
                if a > 0:
                    ret = max(ret, 1 + dp(a-1, b, c, 0))
                if c > 0:
                    ret = max(ret, 1 + dp(a, b, c-1, 2))
                return ret
        ans = 0
        if x > 0:
            ans = max(ans, 1 + dp(x-1, y, z, 0))
        if y > 0:
            ans = max(ans, 1 + dp(x, y-1, z, 1))
        if z > 0:
            ans = max(ans, 1 + dp(x, y, z-1, 2))
        return ans * 2