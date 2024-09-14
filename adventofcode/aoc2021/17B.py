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
        # print(xslices)
        ss = set()
        for yv in range(yl, -yl+1):
            for xv in xslices:
                x = 0
                l = xslices[xv]
                for i in range(l[-1]+1, l[-1]+1000):
                    l.append(i)
                cv = xv
                for i in range(1, l[0]):
                    x += cv
                    cv -= 1
                for step in l:
                    x += cv
                    cv -= 1
                    if x > xr:
                        break
                    found = False
                    if step <= yv+1:
                        y = (yv) * (yv + 1) // 2 - (yv - step) * (yv - step + 1) // 2
                    else:
                        y = (yv) * (yv + 1) // 2 - (step - yv - 1) * (step - yv) // 2
                    if yl <= y <= yr:
                        # print((xv, yv))
                        ss.add((xv, yv))
                        found = True
                        # if yv * (yv + 1) // 2 > ret:
                        #     ret = yv * (yv + 1) // 2
                        #     print(ret, y, xv, step)
                    elif y < yl:
                        break
                    if found:
                        break
        print(len(ss))