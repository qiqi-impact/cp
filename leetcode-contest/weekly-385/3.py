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

PRIMES = get_primes(1000)

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        f = defaultdict(int)
        R, C = len(mat), len(mat[0])
        
        for i in range(R):
            for j in range(C):
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx or dy:
                            cx, cy = i, j
                            cur = 0
                            while 0 <= cx < R and 0 <= cy < C:
                                cur = 10 * cur + mat[cx][cy]
                                cx += dx
                                cy += dy
                                if cur > 10:
                                    f[cur] += 1
        # print(f)
        for x, y in sorted(f.items(), key=lambda t:(-t[1], -t[0])):
            fail = 0
            for p in PRIMES:
                if x == p:
                    break
                if x % p == 0:
                    fail = 1
                    break
            if not fail:
                return x
        return -1
                            
                            