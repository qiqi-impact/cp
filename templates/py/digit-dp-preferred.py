A = [[int(x) for x in str(r)], [int(x) for x in str(l-1)]]

@cache
def dp(idx, lr, lim, st):
    if idx == -1:
        # change this
        return 1
    mx = A[lr][-idx-1]
    ret = 0
    for cur in range(st, (mx if lim else 9) + 1):
        nlim = lim and cur == mx
        # change this
        ret += dp(idx - 1, lr, nlim, 0)
    return ret

ans = 0
for idx in range(2):
    ln = len(A[idx])
    for nd in range(1, ln + 1):
        ans += (-1 ** idx) * dp(nd-1, 0, nd == ln, 1)

dp.cache_clear()

return ans