class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        occ = [0] * 26
        for i in range(len(s)):
            occ[ord(s[i])-97] += 1
        last = None
        ct = 0
        ret = ''
        for i in range(len(s)):
            found = False
            for j in range(25, -1, -1):
                if occ[j] > 0 and (last != j or ct < repeatLimit):
                    ret += chr(j+97)
                    occ[j] -= 1
                    found = True
                    if last == j:
                        ct += 1
                    else:
                        ct = 1
                        last = j
                    break
            if not found:
                break
        return ret