from sortedcontainers import SortedList

class TOPK():
    def __init__(self, top, valfn):
        self.left = SortedList()
        self.right = SortedList()
        self.sm = 0
        self.top = top
        self.valfn = valfn

    def add(self, p):
        self.right.add(p)
        self.sm += self.valfn(p)
        if len(self.right) > self.top:
            p = self.right[0]
            self.sm -= self.valfn(p)
            self.right.remove(p)
            self.left.add(p)

    def discard(self, p):
        if p >= self.right[0]:
            if p in self.right:
                self.sm -= self.valfn(p)
                self.right.remove(p)
            if len(self.right) < self.top and self.left:
                p = self.left[-1]
                self.sm += self.valfn(p)
                self.left.remove(p)
                self.right.add(p)
        else:
            self.left.discard(p)

#---

class BOTK():
    def __init__(self, top, valfn):
        self.left = SortedList()
        self.right = SortedList()
        self.sm = 0
        self.top = top
        self.valfn = valfn

    def add(self, p):
        self.left.add(p)
        self.sm += self.valfn(p)
        if len(self.left) > self.top:
            p = self.left[-1]
            self.sm -= self.valfn(p)
            self.left.remove(p)
            self.right.add(p)

    def discard(self, p):
        if p <= self.left[-1]:
            if p in self.left:
                self.sm -= self.valfn(p)
                self.left.remove(p)
            if len(self.left) < self.top and self.right:
                p = self.right[0]
                self.sm += self.valfn(p)
                self.right.remove(p)
                self.left.add(p)
        else:
            self.right.discard(p)