class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        a, b = toBeRemoved
        ret = []
        for x, y in intervals:
            if x <= a <= b <= y:
                if x != a:
                    ret.append([x,a])
                if y != b:
                    ret.append([b,y])
            elif x <= a <= y:
                if x != a:
                    ret.append([x,a])
            elif x <= b <= y:
                if y != b:
                    ret.append([b,y])
            elif a <= x <= y <= b:
                pass
            else:
                ret.append([x,y])
        return ret