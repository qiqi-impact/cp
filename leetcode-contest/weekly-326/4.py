# algo by pawelb87

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def check_prime(n):
            if n==2 or n==3: return True
            if n%2==0 or n<2: return False
            for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
                if n%i==0:
                    return False    
            return True
        
        ret = math.inf
        p = None
        for a in range(left, right+1):
            if check_prime(a):
                for b in range(a+1, right+1):
                    if b - a >= ret:
                        break
                    elif check_prime(b):
                        ret = b - a
                        p = [a, b]
                        if 0 < ret <= 2:
                            return p
        return p if p else [-1, -1]