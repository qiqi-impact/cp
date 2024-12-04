with open("in") as f:
    ret = 0
    for x in f.read().splitlines():
        l, r = x.split(',')
        a, b = [int(c) for c in l.split('-')]
        c, d = [int(x) for x in r.split('-')]
        if a <= c and d <= b or a >= c and d >= b:
            ret += 1
        else:
            if c <= a <= d or a <= c <= b:
                ret += 1
    print(ret)