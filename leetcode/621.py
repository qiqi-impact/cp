class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for k in tasks:
            d[k] += 1
        h = [(-v, k) for k, v in d.items()]
        heapq.heapify(h)
        rt = {}
        t = 0
        while h or rt:
            if t in rt:
                heapq.heappush(h, rt[t])
                del rt[t]
            if h:
                v, k = heapq.heappop(h)
                if v != -1:
                    rt[t+n+1] = (v+1, k)
            t += 1
        return t