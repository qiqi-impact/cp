class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        l = []
        i = 0
        while True:
            i += 1
            fail = False
            for j in l:
                if j + i == k:
                    fail = True
                    break
            if not fail:
                l.append(i)
                if len(l) == n:
                    return sum(l)