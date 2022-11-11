class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        qty = [1] * n
        for i in range(k-1):
            nq = [1]
            for j in range(1, len(qty)):
                nq.append(nq[-1] + qty[j-1])
                if nq[j] > n:
                    break
            qty = nq
        sm = 0
        for i in range(len(qty)):
            sm += qty[i]
            if sm >= n:
                return i+1