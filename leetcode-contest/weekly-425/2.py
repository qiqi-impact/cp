class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        if n % k != 0:
            return False
        q = n//k
        d = defaultdict(int)
        for i in range(0, n, q):
            d[s[i:i+q]] += 1
            d[t[i:i+q]] -= 1
        for k in d:
            if d[k] != 0:
                return False
        return True