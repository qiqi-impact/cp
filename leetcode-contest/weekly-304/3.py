class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        g = defaultdict(set)
        for i, x in enumerate(edges):
            if x != -1:
                g[i].add(x)
        def dijk(idx):
            ret = [float('inf')] * len(edges)
            ret[idx] = 0
            h = [(0, idx)]
            while h:
                (d, i) = heapq.heappop(h)
                if ret[i] != d:
                    continue
                for o in g[i]:
                    if ret[o] > d + 1:
                        ret[o] = d+1
                        heapq.heappush(h, (d+1, o))
            return ret
        a = dijk(node1)
        b = dijk(node2)
        # print(a, b)
        
        mn = float('inf')
        v = None
        for i in range(len(a)):
            if mn > max(a[i], b[i]):
                mn = max(a[i], b[i])
                v = i
        return v if v is not None else -1