class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        d = defaultdict(dict)
        win = set()
        for x, y in pick:
            if y not in d[x]:
                d[x][y] = 0
            d[x][y] += 1
            if d[x][y] > x:
                win.add(x)
        return len(win)