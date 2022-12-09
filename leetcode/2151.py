class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        N = len(statements)
        
        def try_bin(i):
            b = [int(x) for x in bin(i)[2:].zfill(N)]
            for r in range(N):
                for c in range(N):
                    v = statements[r][c]
                    if v == 1:
                        if b[r] == 1 and b[c] == 0:
                            return False
                    if not v:
                        if b[r] == 1 and b[c] == 1:
                            return False
            return True
        
        ret = 0
        for i in range(2**N):
            if try_bin(i):
                ret = max(ret, i.bit_count())
        return ret