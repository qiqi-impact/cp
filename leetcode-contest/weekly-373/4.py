class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        md = []
        for i in range(k):
            if i*i%k == 0:
                md.append(i)
        
        diff = {0: {0: 1}}
        d = 0
        v = 0
        ret = 0
        for x in s:
            if x in 'aeiou':
                d += 1
                v += 1
            else:
                d -= 1
            if d in diff:
                dd = diff[d]
                for q in md:
                    ret += dd.get((v-q)%k, 0)
            else:
                diff[d] = {}
            diff[d][v%k] = diff[d].get(v%k, 0) + 1
        return ret