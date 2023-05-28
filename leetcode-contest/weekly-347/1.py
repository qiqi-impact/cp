class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        l = [c for c in num]
        while l and l[-1] == '0':
            l.pop()
        return ''.join(l)