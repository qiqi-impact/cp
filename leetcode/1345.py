from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = defaultdict(list)
        for i, x in enumerate(arr):
            d[x].append(i)
        used = set()
        used_idx = set([0])
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            if x == len(arr)-1:
                return y
            v = arr[x]
            if v not in used:
                used.add(v)
                for idx in d[v]:
                    if idx not in used_idx:
                        used_idx.add(idx)
                        q.append((idx, y+1))
            for dx in [-1, 1]:
                nx = x+dx
                if 0 <= nx < len(arr) and nx not in used_idx:
                    used_idx.add(nx)
                    q.append((nx, y+1))
                    