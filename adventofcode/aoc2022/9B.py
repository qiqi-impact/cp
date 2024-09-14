from functools import cache

with open('in') as f:
    ret = 0
    tp = set()
    knots = [[0,0] for _ in range(10)]
    D = {
        'R': [1, 0],
        'U': [0, -1],
        'D': [0, 1],
        'L': [-1, 0]
    }
    tp.add((0, 0))
    for x in f.read().splitlines():
        a, b = x.split(' ')
        dx, dy = D[a]  
        for i in range(int(b)):
            knots[0][0] += dx
            knots[0][1] += dy
            for j in range(9):
                did = False
                hx, hy = knots[j][0], knots[j][1]
                tx, ty = knots[j+1][0], knots[j+1][1]
                xx = abs(hx - tx)
                yy = abs(hy - ty)
                if xx <= 1 and yy <= 1:
                    pass
                elif xx == 2 and yy == 2:
                    did = True
                    tx, ty = (hx+tx)//2, (hy+ty)//2
                    knots[j+1][0], knots[j+1][1] = tx, ty
                else:
                    did = True
                    if hx - tx == 2:
                        tx, ty = hx-1, hy
                    elif hx - tx == -2:
                        tx, ty = hx+1, hy
                    elif hy - ty == 2:
                        tx, ty = hx, hy-1
                    else:
                        tx, ty = hx, hy+1
                    knots[j+1][0], knots[j+1][1] = tx, ty
                # print(knots)
                if not did:
                    break
        # print(knots)
            tp.add((knots[-1][0], knots[-1][1]))
    print(len(tp))