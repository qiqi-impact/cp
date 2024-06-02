class Solution:
    def clearStars(self, s: str) -> str:
        d = defaultdict(list)
        for i, x in enumerate(s):
            if x != '*':
                d[x].append(i)
            else:
                for k in string.ascii_lowercase:
                    if d[k]:
                        d[k].pop()
                        break
        f = {}
        for k in d:
            l = d[k]
            for x in l:
                f[x] = k
                
        ret = ''
        for k in sorted(f.keys()):
            ret += f[k]
        return ret