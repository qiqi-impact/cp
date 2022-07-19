class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ret = []
        def dfs(idx, h, m, t):
            if idx == 10:
                if t == 0:
                    ret.append(str(h) + ':' + str(m).rjust(2, '0'))
                return
            if t:
                nh, nm = h, m
                if idx < 4:
                    nh = h ^ (1 << idx)
                else:
                    nm = m ^ (1 << (idx - 4))
                if nh < 12 and nm < 60:
                    dfs(idx+1, nh, nm, t-1)
            dfs(idx+1, h, m, t)
        dfs(0, 0, 0, turnedOn)
        return ret