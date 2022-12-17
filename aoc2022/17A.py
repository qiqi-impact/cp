
DEPTH = 10000
chamber = [[0 for _ in range(7)] for _ in range(DEPTH)]
for j in range(7):
    chamber[DEPTH-1][j] = 1

# chamber[-3][2] = 1

def pch():
    for i in range(DEPTH):
        s = ''
        for j in range(7):
            s += '#' if chamber[i][j] else '.'
        print(s)

pieces = [
    [[[0, 0], [0, 1], [0, 2], [0, 3]], 4],
    [[[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]], 6],
    [[[0, 2], [1, 2], [2, 0], [2, 1], [2, 2]], 6],
    [[[0, 0], [1, 0], [2, 0], [3, 0]], 7],
    [[[0, 0], [0, 1], [1, 0], [1, 1]], 5],
]

with open('in') as f:
    for l in f.read().splitlines():
        jet = []
        for c in l:
            jet.append((-1 if c == '<' else 1))
# print(jet)

def tryshift(br, dx, dy):
    for x, y in br:
        if not (0 <= y + dy < 7 and ((x + dx, y + dy) in br or chamber[x + dx][y + dy] == 0)):
            return False
    nbr = [(x + dx, y + dy) for (x, y) in br]
    # print(br)
    # print(nbr)
    for x, y in br:
        chamber[x][y] = 0
    for x, y in nbr:
        chamber[x][y] = 1
    return True

jp = 0
top = DEPTH-1
for piece in range(2022):
    pp = piece % len(pieces)
    bricks, gap = pieces[pp]
    cx = top - gap
    cy = 2
    pc = [(cx + x, cy + y) for (x, y) in bricks]
    for x, y in pc:
        chamber[x][y] = 1
    # pch()
    # input()
    # print()
    while 1:
        j = jet[jp]
        pc = [(cx + x, cy + y) for (x, y) in bricks]
        v = tryshift(pc, 0, j)
        # pch()
        if v:
            cy += j
        jp = (1 + jp) % len(jet)
        pc = [(cx + x, cy + y) for (x, y) in bricks]
        v = tryshift(pc, 1, 0)
        # pch()
        # print(j)
        # input()
        if not v:
            break
        else:
            cx += 1
    top = min(top, cx)

pch()
print(DEPTH - 1 - top)