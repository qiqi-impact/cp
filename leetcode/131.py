class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def ispal(i, j):
            if i >= j:
                return True
            return s[i] == s[j] and ispal(i+1, j-1)
        
        @cache
        def dp(idx):
            if idx == len(s):
                return [[]]
            ret = []
            cur = ''
            for i in range(idx, len(s)):
                cur += s[i]
                if ispal(idx, i):
                    for x in dp(i+1):
                        ret.append([cur] + x)
            return ret
        
        return dp(0)