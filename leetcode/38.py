class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n-1):
            c = []
            cur = None
            ln = 0
            for x in s:
                x = int(x)
                if x == cur:
                    ln += 1
                else:
                    if ln:
                        c.append((cur, ln))
                    cur = x
                    ln = 1
            c.append((cur, ln))
            s = ''
            for x, y in c:
                s += str(y) + str(x)
        return s