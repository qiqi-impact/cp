class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        l = [0] * 4
        t = [str(x) for x in [num1, num2, num3]]
        for i in range(3):
            t[i] = ('0' * (4-len(t[i]))) + t[i]
        # print(t)
        ret = ''
        for i in range(4):
            m = inf
            for j in range(3):
                m = min(m, int(t[j][i]))
            ret += str(m)
        return int(ret)