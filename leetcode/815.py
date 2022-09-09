class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        
        buses = defaultdict(list)
        for i in range(len(routes)):
            for x in routes[i]:
                buses[x].append(i)
        
        g = [set() for _ in range(len(routes))]
        for k in buses:
            l = buses[k]
            for i in range(len(l)):
                for j in range(i+1, len(l)):
                    g[l[i]].add(l[j])
                    g[l[j]].add(l[i])
                    
        cost = {}        
        q = deque()
        tgt = set(buses[target])
        for x in buses[source]:
            q.append(x)
            cost[x] = 1
            if x in tgt:
                return 1
        
        while q:
            x = q.popleft()
            for y in g[x]:
                if y not in cost:
                    cost[y] = cost[x] + 1
                    if y in tgt:
                        return cost[y]
                    q.append(y)
        return -1