class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p,q)
        q //= g
        p //= g
        if q%2==0: return 0
        return 1 if p%2 else 2