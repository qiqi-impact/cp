class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        a = [0] * 26
        b = [0] * 26
        for c in word1:
            a[ord(c) - 97] += 1
        for c in word2:
            b[ord(c) - 97] += 1
        
        for i in range(26):
            if a[i]:
                for j in range(26):
                    if b[j]:
                        a[i] -= 1
                        a[j] += 1
                        
                        b[j] -= 1
                        b[i] += 1
                        
                        if sum([int(x > 0) for x in a]) == sum([int(x > 0) for x in b]):
                            return True
                        
                        a[i] += 1
                        a[j] -= 1
                        
                        b[j] += 1
                        b[i] -= 1
        return False