class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        l = [ord(c)-97 for c in s]
        
        def add_at(idx):
            carry = 1
            lm = idx
            for i in range(idx, -1, -1):
                l[i] += carry
                lm = i
                if l[i] == k:
                    l[i] = 0
                    carry = 1
                else:
                    carry = 0
                    break
            if carry == 1:
                return 0, None
            return 1, lm
        
        def fill(idx):
            for i in range(idx, len(l)):
                for t in range(k):
                    if i > 0 and l[i-1] == t:
                        continue
                    if i > 1 and l[i-2] == t:
                        continue
                    l[i] = t
                    break

        if not add_at(len(l)-1)[0]:
            return ''

        i = 1
        while i < len(l):
            need = False
            while l[i] == l[i-1] or (i > 1 and l[i] == l[i-2]):
                need = True
                v, lm = add_at(i)
                if v == 0:
                    return ''
                if v == 1:
                    i = lm-1
                    need = False
                    break
            if need:
                fill(i+1)
                break
            i += 1
        
        return ''.join([chr(97+x) for x in l])