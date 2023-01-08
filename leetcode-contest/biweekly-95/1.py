class Solution:
    def categorizeBox(self, a: int, b: int, c: int, m: int) -> str:
        x = max(a, b, c) >= 10**4 or a*b*c >= 10**9
        y = m >= 100
        if x and y:
            return 'Both'
        elif x:
            return 'Bulky'
        elif y:
            return 'Heavy'
        else:
            return 'Neither'