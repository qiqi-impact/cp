with open("in") as f:
    r = []
    sm = 0
    for x in f.read().splitlines():
        try:
            v = int(x)
            sm += v
        except:
            r.append(sm)
            sm = 0
    print(sum(sorted(r)[-3:]))