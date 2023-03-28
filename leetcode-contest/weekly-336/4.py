class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1])
        take = set()
        for x, y, z in tasks:
            cur = 0
            for i in range(y, x-1, -1):
                if i in take:
                    cur += 1
            if z > cur:
                for i in range(y, x-1, -1):
                    if i not in take:
                        take.add(i)
                        cur += 1
                        if z == cur:
                            break
        return len(take)