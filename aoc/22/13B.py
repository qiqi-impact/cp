
cc = [[[2]], [[6]]]
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
        cc.append(eval(l))

d = {}
for i in range(len(cc)):
    d[i] = 1
    for j in range(len(cc)):
        if check(cc[j], cc[i]) == 1:
            d[i] += 1

print(d[0] * d[1])