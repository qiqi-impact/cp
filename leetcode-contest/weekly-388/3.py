class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        l = []
        ct = defaultdict(int)
        for x in arr:
            s = set()
            for i in range(len(x)):
                for j in range(i, len(x)):
                    s.add((j-i, x[i:j+1]))
            for t in s:
                ct[t[1]] += 1
            l.append(sorted(s))
        
        ret = []
        for i in range(len(l)):
            f = 0
            for _, x in l[i]:
                if ct[x] == 1:
                    ret.append(x)
                    f = 1
                    break
            if not f:
                ret.append('')
        return ret