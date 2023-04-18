class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [None] * k
        self.head = self.tail = 0

    def next(self, ptr):
        return (ptr+1)%len(self.q)

    def prev(self, ptr):
        return (ptr-1+len(self.q))%len(self.q)

    def insertFront(self, value: int) -> bool:
        nx = self.prev(self.head)
        if self.q[nx] is not None:
            return False
        self.head = nx
        self.q[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        nx = self.tail
        if self.q[nx] is not None:
            return False
        self.q[self.tail] = value
        self.tail = self.next(self.tail)
        return True

    def deleteFront(self) -> bool:
        if self.q[self.head] is None:
            return False
        self.q[self.head] = None
        self.head = self.next(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.q[self.head] is None:
            return False
        nx = self.prev(self.tail)
        self.tail = nx
        self.q[self.tail] = None
        return True

    def getFront(self) -> int:
        if self.q[self.head] is None:
            return -1
        return self.q[self.head]

    def getRear(self) -> int:
        if self.q[self.head] is None:
            return -1
        return self.q[self.prev(self.tail)]

    def isEmpty(self) -> bool:
        return self.q[self.head] is None

    def isFull(self) -> bool:
        return self.q[self.tail] is not None


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()