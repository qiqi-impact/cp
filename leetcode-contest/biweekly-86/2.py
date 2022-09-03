class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def f(x, b):
            s = ''
            while x:
                s += str(x%b)
                x //= b
            return s
        for i in range(2, n-1):
            v = f(n, i)
            for j in range(len(v)//2):
                if v[j] != v[len(v)-1-j]:
                    return False
        return True