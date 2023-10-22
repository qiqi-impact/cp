class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        @cache
        def ch(l, r):
            mn = inf
            for m in range(1, r-l+1):
                if (r-l+1) % m != 0:
                    continue
                ss = [''] * m
                for i in range(l, r+1):
                    ss[i%m] += s[i]
                ret = 0
                for x in ss:
                    if len(x) % 2:
                        st = len(x)//2
                        for j in range(st+1):
                            if x[st-j] != x[st+j]:
                                ret += 1
                    else:
                        st = len(x)//2-1
                        for j in range(st+1):
                            if x[st-j] != x[st+j+1]:
                                ret += 1
                mn = min(mn, ret)
            return mn

        @cache
        def dp(idx, left):
            if left < 0:
                return inf
            if idx == n:
                return 0 if left == 0 else inf
            ret = inf
            for i in range(idx+1, n):
                ret = min(ret, ch(idx, i) + dp(i+1, left-1))
            return ret

        return dp(0, k)