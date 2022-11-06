class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort()
        robot.sort()
        
        @cache
        def f(ri, fi):
            if ri == len(robot):
                return 0
            if fi == len(factory):
                return float('inf')
            x, q = factory[fi]
            tot = 0
            ret = f(ri, fi+1)
            for i in range(ri, min(ri+q, len(robot))):
                tot += abs(robot[i] - x)
                ret = min(ret, tot + f(i+1, fi+1))
            return ret
        
        return f(0, 0)