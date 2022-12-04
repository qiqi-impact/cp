with open("in") as f:
    ret = 0
    l = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    for x in f.read().splitlines():
        a, b = [l[t] for t in x.split(' ')]
        if b >= 2:
            ret += 3
        if b == 3:
            ret += 3
        ret += (a%3)+1
    print(ret)