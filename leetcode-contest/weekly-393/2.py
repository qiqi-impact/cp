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

PRIMES = set(get_primes(100))

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        mn = None
        for i in range(len(nums)):
            if nums[i] in PRIMES:
                mn = i
                break
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in PRIMES:
                return i - mn
                
                