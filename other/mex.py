def mexes(a):
    rev = [None] * len(a)
    for i, e in enumerate(a):
        rev[e] = i
    ret = [len(a)*(len(a)+1)//2]
    mx = float('-inf')
    mn = float('inf')
    for i in range(len(rev)):
        mn = min(mn, rev[i])
        mx = max(mx, rev[i])
        v = (mn+1) * (len(a)-mx)
        ret[-1] -= v
        ret.append(v)
    return ret
    
print(mexes([3, 0, 2, 1]))