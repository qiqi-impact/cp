# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ret = [[-1 for _ in range(n)] for _ in range(m)]
        x, y = 0, 0
        dx, dy = 0, 1
        while head:
            ret[x][y] = head.val
            head = head.next
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n or ret[nx][ny] != -1:
                if (dx, dy) == (0, 1):
                    dx, dy = 1, 0
                elif (dx, dy) == (1, 0):
                    dx, dy = 0, -1
                elif (dx, dy) == (0, -1):
                    dx, dy = -1, 0
                else:
                    dx, dy = 0, 1
            x += dx
            y += dy
        return ret