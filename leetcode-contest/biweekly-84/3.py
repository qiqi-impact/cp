class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        recover = {}
        t = 0
        for x in tasks:
            t = 1 + max(recover.get(x, 0), t)
            recover[x] = t + space
        return t