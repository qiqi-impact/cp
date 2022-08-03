def exectime(arr):
    d = {}
    for n in arr:
        if n not in d:
            d[n] = 0
        d[n] += 1
    ret = 0
    for k, v in d.items():
        for i in range(v):
            ret += k
            k = (k+1)//2
    return ret

print(exectime([8,4,4,8,2]))