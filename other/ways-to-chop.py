from functools import cache

@cache
def numways(N, S):
    if N == 0:
        return int(S == 0)
    ret = 0
    for i in range(0, S+1):
        ret += numways(N-1, S-i)
    return ret

print(numways(2, 4))