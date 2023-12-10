class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        MOD = 10**9+7
        n = len(nums)
        
        d = {}
        for i, x in enumerate(nums):
            if x not in d:
                d[x] = [i, i]
            else:
                d[x][1] = i
            
        ivs = list(d.values())
            
        # half-open intervals [a, b)
        def merge(iv):
            ev = defaultdict(int)
            for x, y in iv:
                ev[x] += 1
                ev[y] -= 1
            ks = sorted(ev.keys())
            ret = []
            st = 0
            for k in ks:
                ost = st
                st += ev[k]
                if st and not ost:
                    ret.append([k, None])
                if ost and not st:
                    ret[-1][1] = k
            return ret
        
        tot = 0
        t = merge(ivs)
        for x, y in t:
            tot += y - x + 1
        
        return pow(2, n - tot + len(t) - 1, 10**9+7)