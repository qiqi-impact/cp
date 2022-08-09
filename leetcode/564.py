class Solution:
    def nearestPalindromic(self, n: str) -> str:
        intn = int(n)
        
        left_half_options = list(range(10))
        for i in range(3):
            x = n[:(len(n)+i)//2]
            if not x:
                x = 1
            x = int(x)
            left_half_options += [x-1, x, x+1]
        
        mn = float('inf')
        ret = ''
        
        opts = []
        for odd_length_pal in [True, False]:
            for k in left_half_options:
                right_half = str(k)[::-1]
                if odd_length_pal:
                    right_half = right_half[1:]
                pal = int(str(k) + right_half)
                opts.append(pal)
        opts.sort()
        
        for pal in opts:
            diff = abs(intn - int(pal))
            if diff < mn and diff != 0:
                mn = diff
                ret = str(pal)
        return ret