class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k -= 1
        if n == 1:
            return 0
        pw = 2**(n-2)
        cur = 0
        while pw >= 1:
            if k >= pw:
                cur = 1 - cur
                k -= pw
            pw //= 2
        return cur