class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        s = set()
        h = [(matrix[0][0], 0, 0)]
        s.add((0, 0))
        while k:
            ret, x, y = heapq.heappop(h)
            if x < len(matrix)-1 and (x+1, y) not in s:
                s.add((x+1, y))
                heapq.heappush(h, (matrix[x+1][y], x+1, y))
            if y < len(matrix[0])-1 and (x, y+1) not in s:
                s.add((x, y+1))
                heapq.heappush(h, (matrix[x][y+1], x, y+1))
            k -= 1
        return ret