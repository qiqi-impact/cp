class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        ret = 0
        ur, uc = set(), set()
        for i in range(len(queries)-1, -1, -1):
            t, x, v = queries[i]
            if t == 0:
                if x not in ur:
                    ret += v * (n - len(uc))
                ur.add(x)
            else:
                if x not in uc:
                    ret += v * (n - len(ur))
                uc.add(x)
        return ret