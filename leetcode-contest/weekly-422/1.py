class Solution:
    def isBalanced(self, num: str) -> bool:
        ret = 0
        for i in range(len(num)):
            x = int(num[i])
            if i % 2:
                ret += x
            else:
                ret -= x
        return ret == 0