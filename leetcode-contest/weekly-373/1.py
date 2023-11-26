class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        R, C = len(mat), len(mat[0])
        for i in range(R):
            if i%2:
                for j in range(C):
                    if mat[i][j] != mat[i][(j-k)%C]:
                        return False
            else:
                for j in range(C):
                    if mat[i][j] != mat[i][(j+k)%C]:
                        return False
        return True