class Node:
    def __init__(self, mx, sm):
        self.mx = mx
        self.sm = sm

class BookMyShow:
    def __init__(self, n: int, m: int):
        self.N = 2 ** ceil(log2(n))
        self.t = [Node(0, 0) for _ in range(2 * self.N)]
        self.fr = 0
        self.m = m
        self.avail = [0] * n
        for i in range(n):
            self.update(i, m)

    def update(self, idx, val):
        idx += self.N
        self.t[idx].mx = val
        self.t[idx].sm = val
        idx //= 2
        while idx >= 1:
            self.t[idx].mx = max(self.t[2 * idx].mx, self.t[2 * idx + 1].mx)
            self.t[idx].sm = self.t[2 * idx].sm + self.t[2 * idx + 1].sm
            idx //= 2

    def get_first(self, idx, left, right, val):
        if val > self.t[1].mx:
            return -1
        if left == right:
            return left
        mi = (left + right)//2
        if self.t[2 * idx].mx >= val:
            return self.get_first(2 * idx, left, mi, val)
        else:
            return self.get_first(2 * idx + 1, mi + 1, right, val)

    def get_avail(self, idx, left, right, max_row):
        if left > max_row:
            return 0
        if right <= max_row:
            return self.t[idx].sm
        mi = (left + right) // 2
        return self.get_avail(2 * idx, left, mi, max_row) + self.get_avail(2 * idx + 1, mi + 1, right, max_row)

    def update_fr(self):
        while self.fr < len(self.avail) and self.avail[self.fr] == self.m:
            self.fr += 1

    def gather(self, k: int, maxRow: int) -> List[int]:
        idx = self.get_first(1, 0, self.N-1, k)
        # print(k, maxRow, idx)
        if idx == -1 or idx > maxRow:
            return []
        ret = [idx, self.avail[idx]]
        self.avail[idx] += k
        v = self.m - self.avail[idx]
        self.update(idx, v)
        self.update_fr()
        return ret

    def scatter(self, k: int, maxRow: int) -> bool:
        if self.fr > maxRow:
            return False
        amt = self.get_avail(1, 0, self.N-1, maxRow)
        if amt < k:
            return False
        while k:
            v = min(k, self.m - self.avail[self.fr])
            k -= v
            self.avail[self.fr] += v
            self.update(self.fr, self.m - self.avail[self.fr])
            self.update_fr()
        return True