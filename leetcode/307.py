class Node:
    def __init__(self, l, r):
        self.val = 0
        self.l = l
        self.r = r
        self.left = self.right = None
        if l != r:
            mi = (l+r)//2
            self.left = Node(l, mi)
            self.right = Node(mi+1, r)
    def update(self, idx, val):
        if self.l == self.r:
            self.val = val
            return
        if idx <= self.left.r:
            self.left.update(idx, val)
        else:
            self.right.update(idx, val)
        self.val = self.left.val + self.right.val
    def rangesum(self, l, r):
        if l <= self.l and self.r <= r:
            return self.val
        if r < self.l or l > self.r:
            return 0
        return self.left.rangesum(l, r) + self.right.rangesum(l, r)

class NumArray:

    def __init__(self, nums: List[int]):
        self.node = Node(0, len(nums)-1)
        for i in range(len(nums)):
            self.node.update(i, nums[i])

    def update(self, index: int, val: int) -> None:
        self.node.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.node.rangesum(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)