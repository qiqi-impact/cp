class Solution:
    def longestValidParentheses(self, s: str) -> int:
        d = {0: -1}
        cur = 0
        ret = 0
        for i, x in enumerate(s):
            cur += (1 if x == '(' else -1)
            if x == ')':
                del d[cur+1]
            if cur in d:
                ret = max(ret, i - d[cur])
            else:
                d[cur] = i
        return ret