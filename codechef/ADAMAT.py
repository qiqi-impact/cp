from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    mat = []
    for _ in range(n):
        mat.append([int(x) for x in stdin.readline().split()])
    ret = 0
    for j in range(n-1, 0, -1):
        if int(mat[0][j] == j+1) != 1-ret%2:
            ret += 1
    print(ret)