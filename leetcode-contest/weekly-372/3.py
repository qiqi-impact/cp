class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        t, u = (a >> n)<<n, (b >> n)<<n
        for i in range(n-1, -1, -1):
            aa = (a >> i) & 1
            bb = (b >> i) & 1
            if aa == bb:
                t ^= (1 << i)
                u ^= (1 << i)
            elif t <= u:
                t ^= (1 << i)
            else:
                u ^= (1 << i)

        return (t * u) % (10**9+7)