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
primes = set(get_primes(1000))

class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        cur = 0
        for x in nums:
            while 1:
                if x <= cur:
                    return False
                cur += 1
                if x - cur in primes:
                    break
        return True
[4,9,6,10]
[6,8,11,12]
[5,8,3]
print(Solution().primeSubOperation([6,8,11,12]))