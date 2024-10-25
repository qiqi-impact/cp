def manacher_odd(s):
    n = len(s)
    s = '$' + s + '^'
    p = [0] * (n + 2)
    l, r = 1, 1
    for i in range(1, n+1):
        p[i] = max(0, min(r - i, p[l + r - i]))
        while s[i - p[i]] == s[i + p[i]]:
            p[i] += 1
        if i + p[i] > r:
            l, r = i - p[i], i + p[i]
    return p[1:-1]

def manacher(s):
    t = ''
    for c in s:
        t += '#' + c
    res = manacher_odd(t + '#')
    return res

def check_pali(arr, i, j):
    return arr[i+j+1] >= j-i+1

arr = manacher('abcba')
print(check_pali(arr, 0, 4))