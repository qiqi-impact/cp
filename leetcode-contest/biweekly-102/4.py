class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = [[] for _ in range(n)]
        for e in edges:
            self.addEdge(e)

    def addEdge(self, edge: List[int]) -> None:
        x, y, w = edge
        self.g[x].append((y, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            return 0
        dist = {node1: 0}
        h = [(0, node1)]
        while h:
            d, cur = heapq.heappop(h)
            if dist[cur] != d:
                continue
            if cur == node2:
                return d
            for y, w in self.g[cur]:
                if dist.get(y, inf) > dist[cur] + w:
                    dist[y] = dist[cur] + w
                    heapq.heappush(h, (dist[y], y))
        return -1
                    

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)