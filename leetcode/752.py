from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        sd = set(deadends)
        dist = {'0000': 0}
        q = deque(['0000'])
        while q:
            cur = q.popleft()
            if cur in sd:
                continue
            for i in range(4):
                x = int(cur[i])
                for dx in [-1, 1]:
                    nx = (x+dx)%10
                    ns = cur[:i] + str(nx) + cur[i+1:]
                    if ns not in dist:
                        q.append(ns)
                        dist[ns] = 1 + dist[cur]
                        if ns == target:
                            return dist[ns]
        return -1