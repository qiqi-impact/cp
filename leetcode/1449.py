class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        d = {}
        for i, e in enumerate(cost):
            d[e] = i+1
        l = list(d.items())
        
        def better(a, b):
            if len(a) > len(b):
                return True
            elif len(a) < len(b):
                return False
            else:
                for i in range(len(a)):
                    if a[i] > b[i]:
                        return True
                    elif a[i] < b[i]:
                        return False
            return False
        
        @cache
        def best(tgt):
            if tgt == 0:
                return ''
            ret = None
            for _, (k, v) in enumerate(l):
                nt = tgt - k
                if nt >= 0:
                    b = best(nt)
                    if b is not None and (ret is None or better(str(v) + b, ret)):
                        ret = str(v) + b
            return ret
        
        x = best(target)
        if x is None:
            return '0'
        return x