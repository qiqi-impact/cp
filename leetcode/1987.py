class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9+7
        a, b = 0, 0
        run = 0
        ret = 0
        z = 0
        lst = None
        for c in binary:
            if c == '0':
                z = 1
                if lst != c:
                    a += run
                    run = a
                else:
                    run += a
                ret += a
            else:
                if b == 0:
                    b = 1
                if lst != c:
                    b += run
                    run = b
                else:
                    run += b
                ret += b
            a %= MOD
            b %= MOD
            run %= MOD
            ret %= MOD
            lst = c
        return (ret+z)%MOD