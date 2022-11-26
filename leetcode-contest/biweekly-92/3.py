class Solution:
    def bestClosingTime(self, customers: str) -> int:
        p = 0
        v = 0
        idx = len(customers)
        for i in range(len(customers)-1, -1, -1):
            c = customers[i]
            p += (-1 if c == 'Y' else 1)
            if p >= v:
                idx = i
                v = p
        return idx