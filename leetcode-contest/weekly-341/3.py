class Solution:
    def addMinimum(self, word: str) -> int:
        want = 'abc'
        pt = 0
        ret = 0
        for i in range(len(word)):
            while word[i] != want[pt]:
                ret += 1
                pt = (1+pt)%3
            pt = (1+pt)%3
        if pt != 0:
            ret += 3 - pt
        return ret