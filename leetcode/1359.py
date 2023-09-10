class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9+7
        cur = 1
        need = n
        for i in range(1, 2*n+1):
            k = i
            while k%2 == 0 and need:
                need -= 1
                k //= 2
            cur *= k
            cur %= MOD
        return cur