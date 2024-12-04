
cc = []
idx = 1

def check(a, b):
    for i in range(len(a)):
        if i >= len(b):
            return -1
        aa, bb = a[i], b[i]
        if type(aa) == type(bb) == int:
            if aa > bb:
                return -1
            elif aa < bb:
                return 1
        else:
            if type(aa) == int:
                aa = [aa]
            if type(bb) == int:
                bb = [bb]
            v = check(aa, bb)
            if v:
                return v
    if len(a) < len(b):
        return 1
    return 0

ret = 0
with open('in') as f:
    for l in f.read().splitlines():
        if not l:
            continue
        if len(cc) < 2:
            cc.append(eval(l))
        if len(cc) == 2:
            if check(cc[0], cc[1]) >= 0:
                ret += idx
                print(idx)
            idx += 1
            cc = []
print(ret)