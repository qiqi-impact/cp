class Solution:
    def sortVowels(self, s: str) -> str:
        VOWELS = 'aeiouAEIOU'
        l, v = [], []
        for x in s:
            if x in VOWELS:
                v.append(x)
            l.append(x)
        v.sort(key=lambda x:-ord(x))
        for i in range(len(l)):
            if l[i] in VOWELS:
                l[i] = v.pop()
        return ''.join(l)