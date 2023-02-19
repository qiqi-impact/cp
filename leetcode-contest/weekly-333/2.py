from collections import deque

class Solution:
    def minOperations(self, n: int) -> int:
        if n == 0: return 0
        q = deque([(n, 0)])
        seen = set([n])
        while q:
            x, y = q.popleft()
            cur = 1
            while 1:
                if x & cur or cur > x:
                    v = abs(x - cur)
                    if v not in seen:
                        if v == 0:
                            return y+1
                        seen.add(v)
                        q.append((v, y+1))
                if cur > x:
                    break
                cur *= 2