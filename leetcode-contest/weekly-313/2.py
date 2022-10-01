class LUPrefix:

    def __init__(self, n: int):
        self.pt = 0
        self.vis = [False] * n

    def upload(self, video: int) -> None:
        video -= 1
        self.vis[video] = True
        while self.pt < len(self.vis) and self.vis[self.pt]:
            self.pt += 1

    def longest(self) -> int:
        return self.pt


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()