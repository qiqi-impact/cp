from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.d = {}
        self.rev = {}

    def change(self, index: int, number: int) -> None:
        if index in self.d:
            old = self.d[index]
            self.rev[old].discard(index)
        self.d[index] = number
        if number not in self.rev:
            self.rev[number] = SortedList()
        self.rev[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.rev or len(self.rev[number]) == 0:
            return -1
        return self.rev[number][0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)