class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9+7
        
        num1 = str(int(num1)-1)
        min_sum -= 1
        
        q = [num1[::-1], num2[::-1]]
        
        @cache
        def f(idx, w, mxs):
            if idx == -1:
                return 1
            
            if w == 2:
                mi = 9
            else:
                mi = int(q[w][idx])
            
            ret = 0
            for d in range(min(mxs, mi)+1):
                if d < mi:
                    ret += f(idx-1, 2, mxs-d)
                else:
                    ret += f(idx-1, w, mxs-d)
            return ret
        
        def tot(w, mxs):
            return f(len(q[w])-1, w, mxs)
        
        return (tot(1, max_sum) - tot(0, max_sum) - tot(1, min_sum) + tot(0, min_sum)) % MOD
        