st = 12345
ed = 56789

l = [int(c) for c in st-1]
r = [int(c) for c in ed]

A = [l, r]
@cache
def dp(li, idx, cap):
    a = A[li]
    if idx == len(a):
        return 1
    ret = 0
    mx = 9
    if cap:
        mx = min(mx, a[idx])
    for dig in range(mx+1):
        iscap = cap and dig == a[idx]
        ret += dp(idx+1, iscap)
    return ret

return dp(1, 0, True) - dp(0, 0, True)