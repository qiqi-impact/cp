class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ret = [-1, -1]
        for i in range(len(mat)):
            s = sum(mat[i])
            if s > ret[1]:
                ret = [i, s]
        return ret