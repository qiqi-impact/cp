class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = defaultdict(set)
        for i in range(n):
            subs[manager[i]].add(i)
        
        q = deque([(0, headID)])
        mx = 0
        while q:
            t, idx = q.popleft()
            mx = max(mx, t)
            print(t, idx)
            for s in subs[idx]:
                q.append((t+informTime[idx], s))
        return mx