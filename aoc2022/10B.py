from functools import cache

x = 1
c = 0
rows = []
row = ''

def intersects():
    global c, x
    return c%40 in [x-1, x, x+1]

with open('in') as f:
    for l in f.read().splitlines():
        if l == 'noop':
            if intersects():
                row += '#'
            else:
                row += '.'
            c += 1
        else:
            a, b = l.split(' ')
            b = int(b)

            if intersects():
                row += '#'
            else:
                row += '.'

            c += 1

            if intersects():
                row += '#'
            else:
                row += '.'

            c += 1
            x += b

    print(row[0:40])
    print(row[40:80])
    print(row[80:120])
    print(row[120:160])
    print(row[160:200])
    print(row[200:240])