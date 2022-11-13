class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
       
        while self.left and self.right and -self.left[0] > self.right[0]:
            a = heapq.heappop(self.left)
            b = heapq.heappop(self.right)
            heapq.heappush(self.left, -b)
            heapq.heappush(self.right, -a)
    
        if len(self.left) > len(self.right):
            heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.right[0] - self.left[0])/2
        return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()