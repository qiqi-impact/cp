class Solution:
    def minimumPushes(self, word: str) -> int:
        ret = 0
        for i in range(len(word)):
            ret += i//8 + 1
        return ret