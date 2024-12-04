with open("in") as f:
    ret = 0
    for x in f.read().splitlines():
        l, r = x[:len(x)//2], x[len(x)//2:]
        c = list(set(l) & set(r))[0]
        if 'a' <= c <= 'z':
            ret += ord(c) - ord('a') + 1
        else:
            ret += ord(c) - ord('A') + 27
    print(ret)