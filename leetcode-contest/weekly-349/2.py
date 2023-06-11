class Solution:
    def smallestString(self, s: str) -> str:
        l = [ord(c) for c in s]
        st = False
        for i in range(len(l)):
            if i == len(l)-1 and not st and l[i] == 97:
                l[i] += 25
                break
            if l[i] == 97:
                if st:
                    break
            if l[i] != 97:
                st = True
                l[i] -= 1
        return ''.join([chr(c) for c in l])