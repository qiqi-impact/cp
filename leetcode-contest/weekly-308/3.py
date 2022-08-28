class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        q = []
        lst = [0, 0, 0]
        for i, s in enumerate(garbage):
            v = [0, 0, 0]
            for c in s:
                if c == 'G':
                    v[0] += 1
                    lst[0] = i
                elif c == 'M':
                    v[1] += 1
                    lst[1] = i
                else:
                    v[2] += 1
                    lst[2] = i
            q.append(v)
        ret = sum(q[0])
        for i in range(1, len(q)):
            for j in range(3):
                if i <= lst[j]:
                    ret += travel[i-1] + q[i][j]
        return ret