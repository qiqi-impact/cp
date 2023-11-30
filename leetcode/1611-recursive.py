class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # cost to get 1 at idx and zero out everything from idx-1..0
        def f(idx):
            if idx == -1:
                return 0
            v = (n>>idx)&1
            if v:
                r = g(idx-1)
            else:
                r = f(idx-1) + 2**idx
            return r

        # cost to zero out everything from idx..0
        def g(idx):
            if idx == -1:
                return 0
            v = (n>>idx)&1
            if v:
                r = f(idx-1) + 2**idx
            else:
                r = g(idx-1)
            return r
        
        return g(32)
