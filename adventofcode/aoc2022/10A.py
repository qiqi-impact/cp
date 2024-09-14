from functools import cache

x = 1
c = 0
ptr = 0
pts = [20, 60, 100, 140, 180, 220]
ret = 0
with open('in') as f:
    for l in f.read().splitlines():
        
        if l == 'noop':
            if ptr < len(pts) and pts[ptr] <= c:
                print(x, pts[ptr])
                ret += x * pts[ptr]
                ptr += 1
            c += 1
        else:
            a, b = l.split(' ')
            b = int(b)
            
            if ptr < len(pts) and pts[ptr] <= c + 2:
                print(x, pts[ptr])
                ret += x * pts[ptr]
                ptr += 1
            x += b
            c += 2
        # print(c, x)
    print(ret)