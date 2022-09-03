class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ret = [str(x) for x in list(range(1, 10))]
        for i in range(n-1):
            nr = []
            for x in ret:
                ix = int(x)%10
                l = [ix - k]
                if k != 0:
                    l.append(ix + k)
                for u in l:
                    if 0 <= u <= 9:
                        nr.append(str(x) + str(u))
            ret = nr
            print(ret)
        return [int(x) for x in ret]