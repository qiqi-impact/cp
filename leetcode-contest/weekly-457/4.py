class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        q = deque([(tx, ty, 0)])
        seen = set([(tx, ty)])
        while q:
            x, y, c = q.popleft()
            if (x, y) == (sx, sy):
                return c
            l = []
            if x%2 == 0 and x//2 >= y:
                l.append((x//2, y))
            if y%2 == 0 and y//2 >= x:
                l.append((x, y//2))
            if x >= y and x - y <= y:
                l.append((x - y, y))
            if y >= x and y - x <= x:
                l.append((x, y - x))
            for a, b in l:
                if a < sx or b < sy or (a, b) in seen:
                    continue
                seen.add((a, b))
                q.append((a, b, c+1))
        return -1