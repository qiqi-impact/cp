class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sw = set(wordDict)
        @cache
        def f(idx):
            if idx == len(s):
                return True
            cur = ''
            for i in range(idx, len(s)):
                cur += s[i]
                if cur in sw:
                    if f(i+1):
                        return True
            return False
        return f(0)