class Router:

    def __init__(self, memoryLimit: int):
        self.m = memoryLimit
        self.dest = {}
        self.ds = {}
        self.p = deque()

    def addPacket(self, s: int, d: int, t: int) -> bool:
        if d in self.ds and (t, s) in self.ds[d]:
            return False
        if d not in self.ds:
            self.ds[d] = set()
            self.dest[d] = deque()
        self.ds[d].add((t, s))
        self.dest[d].append((t, s))
        self.p.append([s, d, t])
        if len(self.p) > self.m:
            ret = self.p.popleft()
            s, d, t = ret
            self.ds[d].discard((t, s))
            self.dest[d].popleft()
        return True

    def forwardPacket(self) -> List[int]:
        if not self.p:
            return []
        ret = self.p.popleft()
        s, d, t = ret
        self.ds[d].discard((t, s))
        self.dest[d].popleft()
        return ret
    
    def getCount(self, d: int, s: int, e: int) -> int:
        if d not in self.dest:
            return 0
        a, b = bisect.bisect_left(self.dest[d], (s, -inf)), bisect.bisect_right(self.dest[d], (e, inf))
        return b - a


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)