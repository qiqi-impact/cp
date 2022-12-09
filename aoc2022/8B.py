from functools import cache

with open('in') as f:
    board = []
    ret = 0
    for x in f.read().splitlines():
        board.append([int(x) for x in x])
    R, C = len(board), len(board[0])

    for i in range(1, R-1):
        for j in range(1, C-1):
            v = board[i][j]

            a = 0
            for ii in range(i-1, -1, -1):
                if board[ii][j] < v:
                    a += 1
                elif board[ii][j] <= v:
                    a += 1
                    break

            b = 0
            for ii in range(i+1, R):
                if board[ii][j] < v:
                    b += 1
                elif board[ii][j] <= v:
                    b += 1
                    break
            
            c = 0
            for jj in range(j-1, -1, -1):
                if board[i][jj] < v:
                    c += 1
                elif board[i][jj] <= v:
                    c += 1
                    break
            
            d = 0
            for jj in range(j+1, C):
                if board[i][jj] < v:
                    d += 1
                elif board[i][jj] <= v:
                    d += 1
                    break

            print('-', a, b, c, d)
            ret = max(ret, a*b*c*d)
    print(ret)

            