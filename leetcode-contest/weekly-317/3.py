class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        s = sum([int(x) for x in str(n)])
        if s <= target:
            return 0
        ret = 10**len(str(n)) - n
        
        x = [0] + [int(x) for x in str(n)]
        for i in range(len(x)):
            if x[i] == 9:
                continue
            xx = [0] * len(x)
            xx[:i+1] = x[:i+1]
            xx[i] += 1
            a = ''.join([str(t) for t in xx])
            # print(i, a)
            if sum([int(q) for q in a]) <= target:
                ret = min(ret, int(a) - n)
        return ret