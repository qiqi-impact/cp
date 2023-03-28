class DetectSquares:

    def __init__(self):
        self.d = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.d[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        a, b = point
        ret = 0
        for x, y in list(self.d.keys()):
            if x != a and y != b and abs(x-a) == abs(y-b):
                ret += self.d[x,y] * self.d[a,y] * self.d[x,b]
        return ret

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)