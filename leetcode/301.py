class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        @cache
        def dp(idx, st):
            if idx == len(s):
                return 0 if st == 0 else -inf
            if s[idx] not in '()':
                return dp(idx+1, st)
            ret = dp(idx+1, st)
            if s[idx] == '(':
                ret = max(ret, 1 + dp(idx+1, st+1))
            elif st > 0:
                ret = max(ret, 1 + dp(idx+1, st-1))
            return ret

        dp(0, 0)
        ret = set()

        cur = ''
        st = 0
        def back(idx):
            nonlocal cur, st
            if idx == len(s):
                ret.add(cur)
                return
            if s[idx] not in '()':
                cur += s[idx]
                back(idx+1)
                cur = cur[:-1]
                return
            a = dp(idx+1, st)
            b = -inf
            if s[idx] == '(':
                df = 1
                b = 1 + dp(idx+1, st+1)
            elif st > 0:
                df = -1
                b = 1 + dp(idx+1, st-1)

            if a >= b:
                back(idx+1)
            if b >= a:
                st += df
                cur += s[idx]
                back(idx+1)
                cur = cur[:-1]
                st -= df
        back(0)
        return ret