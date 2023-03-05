class Solution:
    def splitNum(self, num: int) -> int:
        s = str(num)
        l = sorted([int(x) for x in s if x != '0'])
        a, b = 0, 0
        for i in range(len(l)):
            if i % 2 == 0:
                a = 10 * a + l[i]
            else:
                b = 10 * b + l[i]
            # print(a, b)
        return a + b