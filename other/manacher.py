def manacher_odd(s):
    n = len(s)
    s = '$' + s + '^'
    p = [0] * (n+2)
    l, r = 1, 1
    for i in range(1, n+1):
        p[i] = max(0, min(r - i, p[l + (r - i)]))
        while s[i - p[i]] == s[i + p[i]]:
            p[i] += 1
        if i + p[i] > r:
            l, r = i - p[i], i + p[i]
    return p

def manacher(s):
    t = ''
    for c in s:
        t += '#' + c
    t += '#'
    return manacher_odd(t)

S = 'aaaaaaaaaaaaaabbbbbbbbbbbaaaaaaaabbbbababababab'
m = manacher(S)

def query(l, r):
    ll, rr = 2*l+2, 2*r+2
    mid = (ll+rr)//2
    return ll >= mid - m[mid] - 1 and rr <= mid + m[mid] - 1

import random
for i in range(20):
    q = random.sample(range(len(S)), 2)
    x, y = sorted(q)
    print(x, y, query(x, y), S[x:y+1])