class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(m)
        if R%2:
            I, J = R//2, R//2+1
        else:
            I, J = R//2, R//2
        for i in range(I):
            for j in range(J):
                ci = R-1-i
                cj = R-1-j
                m[i][j], m[j][ci], m[ci][cj], m[cj][i] = m[cj][i], m[i][j], m[j][ci], m[ci][cj]
        return m