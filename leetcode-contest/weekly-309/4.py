class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        avail_rooms = list(range(n))
        meeting_over = []
        
        ct = [0] * n
        mtg_queue = []
        mqp = 0
        
        for x, y in meetings:
            mtg_queue.append((x, y-x))
            
        while mqp < len(mtg_queue):
            x, y = mtg_queue[mqp]
            
            while meeting_over and meeting_over[0][0] <= x:
                _, i = heapq.heappop(meeting_over)
                heapq.heappush(avail_rooms, i)
                
            # print(mqp, avail_rooms)
            
            if avail_rooms:
                r = heapq.heappop(avail_rooms)
                ct[r] += 1
                heapq.heappush(meeting_over, (x+y, r))
            else:
                t, i = heapq.heappop(meeting_over)
                heapq.heappush(avail_rooms, i)
                r = heapq.heappop(avail_rooms)
                ct[r] += 1
                heapq.heappush(meeting_over, (t+y, r))
                
            # print(meeting_over)
            mqp += 1
        
        idx = None
        v = 0
        for i in range(n):
            if ct[i] > v:
                idx = i
                v = ct[i]
        # print(ct)
        return idx
        
        