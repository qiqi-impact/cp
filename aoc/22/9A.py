from functools import cache

with open('in') as f:
    ret = 0
    tp = set()
    hx, hy = 0, 0
    tx, ty = 0, 0
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
            hx += dx
            hy += dy
            xx = abs(hx - tx)
            yy = abs(hy - ty)
            if xx <= 1 and yy <= 1:
                pass
            else:
                if hx - tx == 2:
                    tx, ty = hx-1, hy
                elif hx - tx == -2:
                    tx, ty = hx+1, hy
                elif hy - ty == 2:
                    tx, ty = hx, hy-1
                else:
                    tx, ty = hx, hy+1
            tp.add((tx, ty))
    print(len(tp))