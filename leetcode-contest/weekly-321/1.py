class Solution:
    def pivotInteger(self, n: int) -> int:
        s = 0
        for i in range(n+1):
            s += i
        
        t = 0
        for i in range(n+1):
            t += i
            if t * 2 == s + i:
                return i
            
        return -1