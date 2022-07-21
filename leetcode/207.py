class Solution:
    def canFinish(self, n: int, e: List[List[int]]) -> bool:
        ind = [0] * n
        g = defaultdict(set)
        for x, y in e:
            g[x].add(y)
            ind[y] += 1
        ct = 0
        q = deque()
        for i in range(n):
            if ind[i] == 0:
                q.append(i)
        while q:
            ct += 1
            x = q.popleft()
            for y in g[x]:
                ind[y] -= 1
                if ind[y] == 0:
                    q.append(y)
        return ct == n