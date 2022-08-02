class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ret = []
        for r in matrix:
            for e in r:
                ret.append(e)
        ret.sort()
        return ret[k-1]