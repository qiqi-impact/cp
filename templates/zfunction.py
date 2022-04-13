def zf(s):
    n = len(s)
    z = [0] * n
    l,r = 0,0
    for i in range(1, n):
        if i <= r:
            z[i] = min(z[i-l], r-i+1)
        while i+z[i] < n and s[i+z[i]] == s[z[i]]:
            z[i]+=1
        if i+z[i]-1 > r:
            r = i+z[i]-1
            l = i
    return z