class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.p = [parent]
        for i in range(16):
            q = []
            cur = self.p[-1]
            for i in range(len(parent)):
                if cur[i] == -1:
                    q.append(-1)
                else:
                    q.append(cur[cur[i]])
            self.p.append(q)

    def getKthAncestor(self, node: int, k: int) -> int:
        cur = node
        for i in range(16):
            if k & (1 << i):
                cur = self.p[i][cur]
                if cur == -1:
                    break
        return cur


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)