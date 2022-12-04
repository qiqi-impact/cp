class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sm = sum(skill)//(len(skill)//2)
        ret = 0
        avail = defaultdict(int)
        for x in skill:
            if avail[sm-x] > 0:
                ret += x * (sm-x)
                avail[sm-x] -= 1
            else:
                avail[x] += 1
        if sum(avail.values()) > 0:
            return -1
        return ret