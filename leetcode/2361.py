class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        cur = [0, expressCost]
        ret = []
        for i in range(len(regular)):
            cur[0] += regular[i]
            cur[1] += express[i]
            cur[0] = min(cur[0], cur[1])
            cur[1] = min(cur[1], cur[0] + expressCost)
            ret.append(cur[0])
        return ret