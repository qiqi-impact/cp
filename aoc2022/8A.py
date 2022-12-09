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

            block = False
            for ii in range(i-1, -1, -1):
                if board[ii][j] >= v:
                    block = True
                    break
            if not block:
                ret += 1
                continue
            
            block = False
            for ii in range(i+1, R):
                if board[ii][j] >= v:
                    block = True
                    break
            if not block:
                ret += 1
                continue
            
            block = False
            for jj in range(j-1, -1, -1):
                if board[i][jj] >= v:
                    block = True
                    break
            if not block:
                ret += 1
                continue
            
            block = False
            for jj in range(j+1, C):
                if board[i][jj] >= v:
                    block = True
                    break
            if not block:
                ret += 1
                continue

    print(ret + 2 * R + 2 * C - 4)