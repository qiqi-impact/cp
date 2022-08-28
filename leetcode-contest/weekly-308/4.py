class Solution:
    def buildMatrix(self, k: int, rc: List[List[int]], cc: List[List[int]]) -> List[List[int]]:
        ret = [[0 for _ in range(k)] for _ in range(k)]
        
        def make_order(arr):
            g = defaultdict(list)
            ind = [0] * (k+1)
            for a, b in arr:
                g[a].append(b)
                ind[b] += 1

            q = deque()
            order = []
            vis = [0] * (k+1)
            for i in range(1, k+1):
                if ind[i] == 0:
                    q.append(i)
                    order.append(i)
                    vis[i] = True

            while q:
                x = q.popleft()
                for y in g[x]:
                    ind[y] -= 1
                    if ind[y] == 0:
                        q.append(y)
                        order.append(y)
                        vis[y] = True
            
            if sum(ind) > 0:
                return None
                        
            for i in range(1, k+1):
                if not vis[i]:
                    order.append(i)
            return order
        
        a = make_order(rc)
        b = make_order(cc)
        if a is None or b is None:
            return []
        q = {}
        for i, x in enumerate(a):
            q[x] = [i, None]
        for i, x in enumerate(b):
            q[x][1] = i
        
        for i in range(1, k+1):
            x, y = q[i]
            ret[x][y] = i
        return ret
                    
        