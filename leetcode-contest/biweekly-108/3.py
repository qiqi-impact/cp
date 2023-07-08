class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        q = set()
        for i in range(11):
            q.add(5**i)
        
        s = [int(x) for x in s]
        
        @cache
        def dp(idx):
            if idx == len(s):
                return 0
            if s[idx] == 0:
                return inf
            ret = 1 + dp(idx+1)
            cur = 1
            for i in range(idx+1, len(s)):
                cur = 2 * cur + s[i]
                if cur in q:
                    ret = min(ret, 1 + dp(i+1))
            return ret
        ret = dp(0)
        return ret if ret != inf else -1