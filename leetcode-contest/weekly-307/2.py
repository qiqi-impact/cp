class Solution:
    def largestPalindromic(self, num: str) -> str:
        dig = [0] * 10
        for c in num:
            dig[int(c)] += 1
        ret = []
        for i in range(len(dig)-1, -1, -1):
            if not ret and i == 0:
                break
            while dig[i] >= 2:
                ret.append(str(i))
                dig[i] -= 2
        mid = []
        for i in range(len(dig)-1, -1, -1):
            if dig[i] == 1:
                mid.append(str(i))
                break
        if not ret and not mid:
            return '0'
        return ''.join(ret + mid + ret[::-1])