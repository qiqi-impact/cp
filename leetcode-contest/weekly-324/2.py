primes = [2]
for i in range(3, 10**5, 2):
    prime = True
    for p in primes:
        if i%p == 0:
            prime = False
            break
    if prime:
        primes.append(i)

class Solution:
    def smallestValue(self, n: int) -> int:
        seen = set([n])
        mn = cur = n
        while 1:
            sm = 0
            for p in primes:
                while cur % p == 0:
                    sm += p
                    cur //= p
                if p > cur:
                    break
            mn = min(mn, sm)
            if sm in seen:
                return mn
            seen.add(sm)
            cur = sm