class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        ind = [0 for _ in range(n)]
        for x, y in prerequisites:
            g[y].append(x)
            ind[x] += 1
        q = deque()
        for i in range(n):
            if ind[i] == 0:
                q.append(i) 
        ret = []
        while q:
            x = q.popleft()
            ret.append(x)
            for y in g[x]:
                ind[y] -= 1
                if ind[y] == 0:
                    q.append(y)
        return ret if len(ret) == n else []