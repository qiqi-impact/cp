class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        sl = len(strs[0])
        l = [['', i] for i in range(n)]
        ret = 0
        for j in range(sl):
            for i in range(n):
                l[i][0] += strs[i][j]
            l.sort()
            fail = False
            for i in range(n):
                if l[i][1] != i:
                    fail = True
                    ret += 1
                    break
            if fail:
                for i in range(n):
                    l[i][0] = l[i][0][:-1]
            l.sort()
        return ret