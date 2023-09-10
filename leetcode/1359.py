class Solution:
    def countOrders(self, n: int) -> int:
        ret = 1
        for i in range(1, 2*n+1):
            ret *= i
            if i%2 == 0:
                ret //= 2
            ret %= (10**9+7)
        return ret