from collections import defaultdict

with open('in') as f:
    for line in f.read().splitlines():
        a,b = line[15:].split(', y=')
        xl, xr = [int(t) for t in a.split('..')]
        yl, yr = [int(t) for t in b.split('..')]
        xslices = defaultdict(list)
        for xv in range(1, xr+1):
            step = 0
            x = 0
            v = xv
            while 1:
                step += 1
                x += v
                v -= 1
                if xl <= x <= xr:
                    xslices[xv].append(step)
                if x > xr or v == 0:
                    break
        print(xslices)
        ret = 0
        for yv in range(1, -yl+1):
            for xv in xslices:
                l = xslices[xv]
                for i in range(l[-1]+1, l[-1]+1000):
                    l.append(i)
                for step in l:
                    if step <= yv+1:
                        y = (yv) * (yv + 1) // 2 - (yv - step) * (yv - step + 1) // 2
                    else:
                        y = (yv) * (yv + 1) // 2 - (step - yv - 1) * (step - yv) // 2
                    if yl <= y <= yr:
                        if yv * (yv + 1) // 2 > ret:
                            ret = yv * (yv + 1) // 2
                            print(ret, y, xv, step)
                    elif y < yl:
                        break
        print(ret)