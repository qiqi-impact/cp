class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        ret = 1
        s = {delay: 1}
        k = {forget: 1}
        tell = 0
        for i in range(1, n):
            if i in k:
                ret -= k[i]
                tell -= k[i]
            if i in s:
                tell += s[i]
            ret += tell
            s[i+delay] = tell
            k[i+forget] = tell
            ret %= (10**9+7)
        return ret