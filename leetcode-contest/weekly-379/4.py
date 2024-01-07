class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        s = [ord(c)-97 for c in s]
        @cache
        def dp(idx, left, seen):
            if idx == len(s):
                return 0
            
            
            ss = seen | (1 << s[idx])
            bc = ss.bit_count()
            if bc > k:
                ret = 1 + dp(idx+1, left, 1 << s[idx])
            else:
                ret = dp(idx+1, left, ss)
            
            if left:
                for i in range(26):
                    ss = seen | (1 << i)
                    bc = ss.bit_count()
                    if bc > k:
                        ret = max(ret, 1 + dp(idx+1, left-1, 1 << i))
                    else:
                        ret = max(ret, dp(idx+1, left-1, ss))
            return ret
        return dp(0, 1, 0)+1