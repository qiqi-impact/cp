from sortedcontainers import SortedList

class Allocator:

    def __init__(self, n: int):
        self.sl = SortedList()
        self.bid = defaultdict(list)
        self.sl.add((n, n, -1))
        
    def allocate(self, size: int, mID: int) -> int:
        cur = 0
        for x, y, z in self.sl:
            sp = x - cur
            if sp >= size:
                a, b, c = (cur, cur + size - 1, mID)
                self.sl.add((a, b, c))
                self.bid[c].append((a, b))
                # print(self.sl)
                return a
            else:
                cur = y + 1
        return -1

    def free(self, mID: int) -> int:
        ret = 0
        for x, y in self.bid[mID]:
            ret += y - x + 1
            self.sl.discard((x, y, mID))
        del self.bid[mID]
        return ret

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)