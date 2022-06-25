class Solution:
    def countAsterisks(self, s: str) -> int:
        l = s.split('|')
        ret = 0
        for i in range(0, len(l), 2):
            ret += l[i].count('*')
        return ret