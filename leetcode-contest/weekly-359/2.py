class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        s = set()
        i = 0
        while True:
            i += 1
            fail = False
            if k - i in s:
                fail = True
            if not fail:
                s.add(i)
                if len(s) == n:
                    return sum(s)