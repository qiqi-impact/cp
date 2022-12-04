with open("in") as f:
    ret = 0
    l = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    for x in f.read().splitlines():
        a, b = [l[t] for t in x.split(' ')]
        ret += b
        if b - a == 1 or (b == 1 and a == 3):
            ret += 6
        elif b == a:
            ret += 3
    print(ret)