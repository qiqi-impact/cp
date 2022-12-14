R, C = 200, 1000

g = [[0 for _ in range(C)] for _ in range(R)]
mxdepth = 0

with open('in') as f:
    for l in f.read().splitlines():
        p = l.split(' -> ')
        pp = [(int(b), int(a)) for (a, b) in [x.split(',') for x in p]]
        for i in range(len(pp)-1):
            a, b = pp[i]
            c, d = pp[i+1]
            if a < c:
                y = b
                for x in range(a, c+1):
                    g[x][y] = 1
            elif a > c:
                y = b
                for x in range(a, c-1, -1):
                    g[x][y] = 1
            elif b < d:
                x = a
                for y in range(b, d+1):
                    g[x][y] = 1
            elif b > d:
                x = a
                for y in range(b, d-1, -1):
                    g[x][y] = 1
            else:
                g[a][b] = 1
            mxdepth = max(mxdepth, a, c)

def simulate(x, y):
    if g[x+1][y] == 0:
        return x+1, y
    elif g[x+1][y-1] == 0:
        return x+1, y-1
    elif g[x+1][y+1] == 0:
        return x+1, y+1
    return x, y

for ct in range(1000000):
    cx, cy = 0, 500
    cont = False
    while 1:
        nx, ny = simulate(cx, cy)
        if nx > mxdepth:
            print(ct)
            break
        if (nx, ny) == (cx, cy):
            g[nx][ny] = 1
            cont = True
            break
        cx, cy = nx, ny
    if not cont:
        break