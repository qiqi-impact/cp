class Solution:
    def possibleStringCount(self, word: str) -> int:
        run = 0
        lst = None
        ret = 1
        for x in word:
            if x == lst:
                run += 1
            else:
                ret += max(0, run - 1)
                run = 1
            lst = x
        ret += max(0, run - 1)
        return ret