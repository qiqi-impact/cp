class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        n = len(nums)
        @cache
        def dp(idx, p, mxp, kl):
            # print(idx, p, mxp, kl)
            if idx == n:
                return -inf if (kl != k or mxp == 0 or p == 2) else 1
            ret = dp(idx+1, p, mxp, kl)
            if p == 2:
                p = 0
            v = nums[idx]
            if p:
                if v == 0:
                    if dp(idx+1, 1-p, inf, kl) != -inf:
                        ret = max(ret, 0)
                elif v <= mxp:
                    ret = max(ret, v * dp(idx+1, 1-p, mxp // v if mxp != inf else mxp, kl - v))
                else:
                    ret = max(ret, v * dp(idx+1, 1-p, 0, kl - v))
            else:
                if v == 0:
                    if dp(idx+1, 1-p, inf, kl) != -inf:
                        ret = max(ret, 0)
                elif v <= mxp:
                    ret = max(ret, v * dp(idx+1, 1-p, mxp // v if mxp != inf else mxp, kl + v))
                else:
                    ret = max(ret, v * dp(idx+1, 1-p, 0, kl + v))
            return ret
        q = dp(0, 2, limit, 0)
        dp.cache_clear()
        return q if q != -inf else -1©leetcode