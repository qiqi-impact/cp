# half-open intervals [a, b)
def merge(iv):
    ev = defaultdict(int)
    for x, y in iv:
        ev[x] += 1
        ev[y] -= 1
    ks = sorted(ev.keys())
    ret = []
    st = 0
    for k in ks:
        ost = st
        st += ev[k]
        if st and not ost:
            ret.append([k, None])
        if ost and not st:
            ret[-1][1] = k
    return ret