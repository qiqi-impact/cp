with open("in") as f:
    ret = 0
    md = 0
    s = None
    for x in f.read().splitlines():
        md += 1
        if md % 3 == 1:
            s = set(x)
        elif md % 3 == 0:
            s &= set(x)
            c = list(s)[0]
            if 'a' <= c <= 'z':
                ret += ord(c) - ord('a') + 1
            else:
                ret += ord(c) - ord('A') + 27
        else:
            s &= set(x)
    print(ret)