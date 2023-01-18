class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lis = []
        ret = []
        for o in obstacles:
            idx = bisect.bisect(lis, o)
            if idx == len(lis):
                lis.append(o)
            else:
                lis[idx] = o
            ret.append(idx+1)
        return ret