class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        def ans(x):
            ct = 0
            for c in s:
                if c in string.ascii_lowercase:
                    ct += 1
                    if ct == x:
                        return c
                else:
                    c = int(c)
                    xct = ct * c
                    if xct >= x:
                        x %= ct
                        if x == 0:
                            x = ct
                        return ans(x)
                    ct = xct
        return ans(k)