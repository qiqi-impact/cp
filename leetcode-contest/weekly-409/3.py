class Node:
    def __init__(self, v):
        self.val = v
        self.next = None

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        l = [Node(i) for i in range(n)]
        for i in range(n-1):
            l[i].next = l[i+1]
        cur = n - 1
        r = []
        for x, y in queries:
            if not l[x] or not l[y]:
                r.append(cur)
                continue
            q = 0
            c = l[x].next
            while c != l[y]:
                q += 1
                t = c.next
                l[c.val] = None
                c = t
            l[x].next = l[y]
            cur -= q
            r.append(cur)
            # print(l)
        return r