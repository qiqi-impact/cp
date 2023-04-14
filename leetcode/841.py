class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        vis = set()
        while q:
            cur = q.popleft()
            vis.add(cur)
            for nx in rooms[cur]:
                if nx not in vis:
                    vis.add(nx)
                    q.append(nx)
        return len(vis) == len(rooms)