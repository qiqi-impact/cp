class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        sf = set(forbidden)
        mx = -1
        ret = 0
        s = ''
        for j in range(len(word)):
            if len(s) == 10:
                s = s[1:]
            s += word[j]
            for i in range(1, 11):
                if j-i+1 < 0:
                    break
                if s[-i:] in sf:
                    mx = max(mx, j-i+1)
                    break
            ret = max(ret, j - mx)
        return ret