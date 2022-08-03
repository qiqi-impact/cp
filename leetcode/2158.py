class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        events = defaultdict(set)
        for i, (x, y) in enumerate(paint):
            events[x].add(i)
            events[y].add(i)
        times = sorted(list(events.keys()))
        in_progress = set()
        h = []
        worklog = [0] * len(paint)
        for i in range(len(times)):
            if h:
                worklog[h[0]] += times[i] - times[i-1]
            ev = events[times[i]]
            for x in ev:
                if x in in_progress:
                    in_progress.discard(x)
                else:
                    in_progress.add(x)
                    heapq.heappush(h, x)
            while h and h[0] not in in_progress:
                heapq.heappop(h)
        return worklog