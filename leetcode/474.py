class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = [(x.count('0'), x.count('1')) for x in strs]

        @cache
        def dp(idx, a, b):
            if idx == len(l):
                return 0
            ret = dp(idx+1, a, b)
            if l[idx][0] <= a and l[idx][1] <= b:
                ret = max(ret, 1 + dp(idx+1, a - l[idx][0], b - l[idx][1]))
            return ret

        return dp(0, m, n)