class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = [c for c in s]
        for i in range(len(l)//2):
            if l[i] != l[len(l)-1-i]:
                l[i] = min(l[i], l[len(l)-1-i])
                l[len(l)-1-i] = l[i]
        return ''.join(l)