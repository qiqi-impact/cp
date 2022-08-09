class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        neg = s[0] == '-'
        if neg:
            s = s[1:]
        s = s[::-1]
        n = int(s)
        if neg:
            n = -n
        return n if -2**31 <= n < 2**31 else 0