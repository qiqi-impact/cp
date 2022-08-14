class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pl = len(pattern)
        ret = [i+1 for i in range(pl+1)]
        dl = 0
        pattern += 'I'
        for i in range(pl+1):
            if pattern[i] == 'D':
                dl += 1
            else:
                rv = ret[i-dl:i+1][::-1]
                for j in range(i-dl, i+1):
                    ret[j] = rv[j-(i-dl)]
                dl = 0
        return ''.join([str(x) for x in ret])