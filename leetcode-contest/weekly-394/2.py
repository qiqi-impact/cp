class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        U, L = string.ascii_uppercase, string.ascii_lowercase
        lst = {}
        for i, c in enumerate(word):
            if c in U:
                if c not in lst:
                    lst[c] = i
            else:
                lst[c] = i
        ret = 0
        for i in range(26):
            x, y = U[i], L[i]
            if x in lst and y in lst and lst[y] < lst[x]:
                ret += 1
        return ret