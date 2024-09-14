from functools import cache

with open('in') as f:
    board = []
    ret = 0
    for x in f.read().splitlines():
        board.append([int(x) for x in x])
    R, C = len(board), len(board[0])

    for i in range(R):
        for j in range(C):
            v = board[i][j]

            a = 0
            for ii in range(i-1, -1, -1):
                a += 1
                if board[ii][j] >= v:
                    break
            a = max(a, 1)
            
            b = 0
            for ii in range(i+1, R):
                b += 1
                if board[ii][j] >= v:
                    break
            b = max(b, 1)

            c = 0
            for jj in range(j-1, -1, -1):
                c += 1
                if board[i][jj] >= v:
                    break
            c = max(c, 1)
            
            d = 0
            for jj in range(j+1, C):
                d += 1
                if board[i][jj] >= v:
                    break
            d = max(d, 1)
            
            ret = max(ret, a*b*c*d)

    print(ret)