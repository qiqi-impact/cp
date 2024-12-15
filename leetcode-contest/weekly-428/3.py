import random

HMOD = 2147483647
HBASE1 = random.randrange(HMOD)

class Hashing:
    def __init__(self, s, mod=HMOD, base1=HBASE1):
        self.mod, self.base1 = mod, base1
        self._len = _len = len(s)
        f_hash, f_pow = [0] * (_len + 1), [1] * (_len + 1)
        for i in range(_len):
            f_hash[i + 1] = (base1 * f_hash[i] + s[i]) % mod
            f_pow[i + 1] = base1 * f_pow[i] % mod
        self.f_hash, self.f_pow = f_hash, f_pow

    def hashed(self, start, stop):
        return (self.f_hash[stop] - self.f_pow[stop - start] * self.f_hash[start]) % self.mod

    def get_hashes(self, length):
        return [(self.f_hash[i + length] - self.f_pow[length] * self.f_hash[i]) % self.mod for i in range(self._len - length + 1)]

class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        h = Hashing(nums)
        n = len(nums)
        ret = 0
        for i in range(1, n-1):
            for j in range(i+1, n):
                a, b, c = i, j-i, n-j
                if (b >= a and h.hashed(0, i) == h.hashed(i, i+a)) or (c >= b and h.hashed(i, j) == h.hashed(j, j+b)):
                    ret += 1
        return ret
        