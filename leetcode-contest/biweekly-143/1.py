class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
         for i in range(n, 10**9):
             l = [int(x) for x in str(i)]
             ret = 1
             for x in l:
                 ret *= x
                 if ret % t == 0:
                     return i