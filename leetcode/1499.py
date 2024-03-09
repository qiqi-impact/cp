class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = deque()
        ret = -inf
        for xj, yj in points:
            while q and q[0][1] + k < xj:
                q.popleft()
            if q:
                ret = max(ret, q[0][0] + xj + yj)
            cur = (yj-xj, xj)
            while q and q[-1][0] < cur[0]:
                q.pop()
            q.append(cur)
        return ret