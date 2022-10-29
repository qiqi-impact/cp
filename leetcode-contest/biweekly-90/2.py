class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ret = []
        for q in queries:
            for d in dictionary:
                dif = 0
                for i in range(len(q)):
                    if q[i] != d[i]:
                        dif += 1
                if dif <= 2:
                    ret.append(q)
                    break
        return ret