class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        h = []
        cur = 0
        for x, y in courses:
            if cur + x > y:
                if h and -h[0] > x:
                    t = heapq.heappop(h)
                    heapq.heappush(h, -x)
                    cur += x + t
            else:
                heapq.heappush(h, -x)
                cur += x
        return len(h)