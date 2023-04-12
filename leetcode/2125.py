class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        l = [x.count('1') for x in bank]
        l = [x for x in l if x != 0]
        ret = 0
        for i in range(1, len(l)):
            ret += l[i] * l[i-1]
        return ret