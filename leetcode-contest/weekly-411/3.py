class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        m = [1]
        for i in range(1, n):
            m.append(m[-1]*10%k)
        
        s = 9 * (sum(m)) % k
        
        if k in [1,3,9]:
            return '9' * n
        
        if k == 2:
            if n == 1:
                return '8'
            return '8' + ('9' * (n-2)) + '8'
        
        if k == 4:
            if n == 1:
                return '8'
            if n == 2:
                return '88'
            if n == 3:
                return '888'
            return '88' + ('9' * (n-4)) + '88'
        
        if k == 8:
            if n <= 6:
                return '8' * n
            return '888' + ('9' * (n-6)) + '888'
        
        if k == 5:
            if n <= 2:
                return '5' * n
            return '5' + ('9' * (n-2)) + '5'
        
        if k == 6:
            if n <= 2:
                return '6' * n
            if n == 4:
                return '8778'
            if n % 2:
                s -= 2
                s %= k
                return '8' + ('9' * ((n-2)//2)) + (str(9 - s)) + ('9' * ((n-2)//2)) + '8'
            s -= m[0] + m[-1]
            s %= k
            v = (m[n//2] + m[n//2-1])%k
            q = (m[n//2+1] + m[n//2-2])%k
            
            for a in range(9, -1, -1):
                for b in range(9, -1, -1):
                    if ((9-a) * q + (9-b) * v) % k == s:
                        return '8' + ('9' * ((n-6)//2)) + str(a) + str(b) + str(b) + str(a) + ('9' * ((n-6)//2)) + '8'
        
        if k == 7:
            if n <= 2:
                return '7' * n
            if n % 2:
                v = (m[n//2])%k
                t = 9
                while s != 0:
                    s = (s - v) % k
                    t -= 1
                return ('9' * (n//2)) + (str(t)) + ('9' * (n//2))
            else:
                v = (m[n//2] + m[n//2-1])%k
                q = (m[n//2+1] + m[n//2-2])%k

                for a in range(9, -1, -1):
                    for b in range(9, -1, -1):
                        if ((9-a) * q + (9-b) * v) % k == s:
                            return ('9' * ((n-4)//2)) + str(a) + str(b) + str(b) + str(a) + ('9' * ((n-4)//2))

            
            