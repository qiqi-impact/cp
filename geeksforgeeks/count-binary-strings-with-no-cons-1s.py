MOD = 10**9+7

#User function Template for python3
class Solution:
    def countStrings(self, N):
        M = [[[0,1],[1,1]]]
        
        def mm(m):
            [[a,b],[c,d]] = m
            return [[(a*a+b*c)%MOD, (a*b+b*d)%MOD],[(c*a+d*c)%MOD, (c*b+d*d)%MOD]]
        
        def mult(m, v):
            [[a,b],[c,d]] = m
            [e,f] = v
            return [(a*e + b*f)%MOD, (c*e + d*f)%MOD]
        
        for i in range(100):
            M.append(mm(M[-1]))
            
        v = [1, 1]
        for i in range(99, -1, -1):
            if N & (1 << i):
                v = mult(M[i], v)
        return v[-1]