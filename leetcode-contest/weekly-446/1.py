class Solution:
    def calculateScore(self, ins: List[str], val: List[int]) -> int:
        cur = 0
        n = len(ins)
        ret = 0
        used = set()
        while 0 <= cur < n and cur not in used:
            used.add(cur)
            if ins[cur] == 'add':
                ret += val[cur]
                cur += 1
            else:
                cur += val[cur]
        return ret