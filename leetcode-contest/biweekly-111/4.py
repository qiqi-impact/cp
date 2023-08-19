class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        low -= 1
        
        l, r = [int(x) for x in str(low)], [int(x) for x in str(high)]
        
        ev, od = [], []
        for i in range(1, 10):
            if i%2:
                od.append(i)
            else:
                ev.append(i)
        
        @cache
        def f(idx, which, nodd, ndig, cur):
            if idx == ndig:
                return cur == 0
            co, ce, cz = True, True, True
            neven = idx - nodd
            left = ndig - idx
            if nodd + left == ndig//2:
                ce = False
            if neven + left == ndig//2:
                co = False
            if idx == 0:
                cz = False
            
            opts = []
            if co:
                opts += od
            if ce:
                opts += ev
            if cz and ce:
                opts.append(0)
            
            ret = 0
            for x in opts:
                nw = which
                if which == 0 and x != l[idx]:
                    nw = 2
                if which == 1 and x != r[idx]:
                    nw = 2
                if (which == 0 and x <= l[idx]) or (which == 1 and x <= r[idx]) or which == 2:
                    ret += f(idx+1, nw, nodd + x%2, ndig, (10*cur+x)%k)
            return ret
        
        ans = 0
        for nd in [2, 4, 6, 8]:
            if nd < len(r):
                ans += f(0, 2, 0, nd, 0)
            elif nd == len(r):
                ans += f(0, 1, 0, nd, 0)
        
        for nd in [2, 4, 6, 8]:
            if nd < len(l):
                ans -= f(0, 2, 0, nd, 0)
            elif nd == len(l):
                ans -= f(0, 0, 0, nd, 0)
        
        return ans