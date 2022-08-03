class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = set()
        c = set()
        for i in range(len(matrix)):
            found = False
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    found = True
            if found:
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 0:
                        matrix[i][j] = None
                    else:
                        matrix[i][j] = 0
        for j in range(len(matrix[0])):
            found = False
            for i in range(len(matrix)):
                if matrix[i][j] is None:
                    found = True
            if found:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        
                