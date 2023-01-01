def get_primes(n):
    p = 3
    sieve = [1 for _ in range(n+1)]
    while p*p <= n:
        if sieve[p]:
            for x in range(p*p, n+1, 2*p):
                sieve[x] = 0
        p += 2
    ret = [2]
    for i in range(3, n+1, 2):
        if sieve[i]:
            ret.append(i)
    return ret
            
p = get_primes(10**6)
diff = []
for i in range(len(p)-1):
    diff.append((p[i+1] - p[i], p[i]))
diff.sort()

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        for d, x in diff:
            if left <= x and x+d <= right:
                return [x, x+d]
        return [-1, -1]