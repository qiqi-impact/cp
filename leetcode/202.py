class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while 1:
            l = [int(x)**2 for x in str(n)]
            q = sum(l)
            if q == 1:
                return True
            if q in s:
                return False
            s.add(q)
            n = q