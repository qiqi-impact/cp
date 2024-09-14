with open("in") as f:
    mx = 0
    sm = 0
    for x in f.read().splitlines():
        try:
            v = int(x)
            sm += v
        except:
            mx = max(mx, sm)
            sm = 0
    mx = max(mx, sm)
    print(mx)