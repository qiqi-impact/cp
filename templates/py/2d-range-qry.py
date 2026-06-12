class Node:
    def __init__(self, m, a, b, c, d):
        l, r = (a+c)//2, (b+d)//2
        self.bounds = (a, b, c, d)
        self.q1 = self.q2 = self.q3 = self.q4 = None
        if a == c and b == d:
            self.value = m[a][b]
        elif a == c:
            self.q1 = Node(m, a, b, a, r)
            self.q2 = Node(m, a, r+1, a, d)
            self.value = max(self.q1.value, self.q2.value)
        elif b == d:
            self.q1 = Node(m, a, b, l, b)
            self.q2 = Node(m, l+1, b, c, b)
            self.value = max(self.q1.value, self.q2.value)
        else:
            self.q1 = Node(m, a, b, l, r)
            self.q2 = Node(m, l+1, b, c, r)
            self.q3 = Node(m, a, r+1, l, d)
            self.q4 = Node(m, l+1, r+1, c, d)
            self.value = max(self.q1.value, self.q2.value, self.q3.value, self.q4.value)
    def mx(self, a, b, c, d):
        aa, bb, cc, dd = self.bounds
        if a <= aa and b <= bb and c >= cc and d >= dd:
            return self.value
        if a > cc or c < aa or b > dd or d < bb:
            return -inf
        m = -inf
        for t in self.q1, self.q2, self.q3, self.q4:
            if t:
                m = max(m, t.mx(a, b, c, d))
        return m