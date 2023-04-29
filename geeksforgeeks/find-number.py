class Solution:
    def findNumber(self, N : int) -> int:
        N -= 1
        dig = 1
        while N >= pow(5, dig):
            N -= pow(5, dig)
            dig += 1
        
        ret = ''
        for i in range(dig-1, -1, -1):
            pw = pow(5, i)
            k = N // pw
            ret += str(2*k+1)
            N -= pw * k
        return str(ret)