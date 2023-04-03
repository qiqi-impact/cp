def plus_minus_helper(s):
    l = [int(x) for x in s]
    q = [((), 2 * l[0] - sum(l))]

    if q[0][1] == 0:
        return set()

    qp = 0
    while qp < len(q):
        t, sm = q[qp]
        t = set(t)
        for i in range(1, len(l)):
            if i not in t:
                nsm = sm + 2 * l[i]
                if nsm == 0:
                    return t | set([i])
                q.append((tuple(sorted(list(t) + [i])), nsm))
        qp += 1
    return None

def plus_minus(s):
    x = plus_minus_helper(s)
    if x is None:
        return 'Not valid'
    ret = ''
    for i in range(1, len(s)):
        if i in x:
            ret += '+'
        else:
            ret += '-'
    return ret

print(plus_minus('3722'))