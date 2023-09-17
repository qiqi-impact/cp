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
PRIMES = get_primes(10**2)


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(int)
        for x in range(1, n+1):
            left = 1
            xx = x
            for p in PRIMES:
                ct = 0
                while xx%p == 0:
                    xx //= p
                    ct += 1
                if ct%2:
                    left *= p
            left *= xx
            d[left] += nums[x-1]
        return max(d.values())
                