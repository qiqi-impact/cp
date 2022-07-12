import functools

@functools.cache
def p(n, k, limit):
    if k >= limit:
        return 0
    if n == 1:
        return 1
    return 1/n*p(n-1, 0, limit) + (n-1)/n*p(n-1, k+1, limit)

for N in range(2, 102, 2):
    print(N, p(N, 0, N//2))