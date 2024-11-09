class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        pf = [0,0,0,0]
        pr = [2,3,5,7]
        for i in range(4):
            while t % pr[i] == 0:
                t //= pr[i]
                pf[i] += 1
        if t != 1:
            return '-1'

        DIFF = [None, [0,0,0,0], [1,0,0,0], [0,1,0,0], [2,0,0,0], [0,0,1,0], [1,1,0,0], [0,0,0,1], [3,0,0,0], [0,2,0,0]]

        def stringify(req):
            s = ''
            for i in range(1, 10):
                s += str(i) * req.get(i, 0)
            return s
        
        left = pf[:]
        def smallest(digits, is_restricted):
            if digits == 0:
                if max(pf) <= 0:
                    return ''
                return
            if not is_restricted:
                pff = [max(0, x) for x in pf]
                req = {5: pff[2], 7:pff[3]}
                req[8] = pff[0] // 3
                req[9] = pff[1] // 2
                a, b = pff[0] % 3, pff[1] % 2
                if a and b:
                    req[6] = 1
                    a -= 1
                    b -= 1
                if b:
                    req[3] = 1
                if a == 2:
                    req[4] = 1
                elif a == 1:
                    req[2] = 1
                req[1] = digits - sum(req.values())
                if req[1] < 0:
                    return
                return stringify(req)
            else:
                st = int(num[len(num) - digits])
                if st != 0:
                    for i in range(4):
                        pf[i] -= DIFF[st][i]
                    q = smallest(digits - 1, True)
                    for i in range(4):
                        pf[i] += DIFF[st][i]
                    if q is not None:
                        return str(st) + q
                while st < 9:
                    st += 1
                    for i in range(4):
                        pf[i] -= DIFF[st][i]
                    q = smallest(digits - 1, False)
                    if q is not None:
                        return str(st) + q
                    for i in range(4):
                        pf[i] += DIFF[st][i]
                return
        q = smallest(len(num), True)
        cur = len(num) + 1
        while not q:
            q = smallest(cur, False)
            cur += 1
        return q