class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        sq = set() # the set of numbers we have to find in s
        mq = 0
        for x, y in queries:
            sq.add(x ^ y)
            mq = max(mq, x ^ y)
        ans = {}
        cur = {} # key = value of digit string up to this point, value = length of that digit string
        for i, x in enumerate(s):
            t = int(x)
            ncur = {t: 1} # just use current digit
            if t in sq:
                ans[t] = [i, i]
                sq.discard(t)
            for y in cur:
                v = y * 2 + t # try appending current digit to some previous digit string
                ncur[v] = cur[y] + 1
                if v in sq:
                    ans[v] = [i - ncur[v] + 1, i]
                    sq.discard(v)
            if 0 in ncur:
                del ncur[0] # never append to 0 because we want the shortest possible string, and an extra 0 on the left is suboptimal
            cur = {}
            for k in ncur:
                if k < mq: # pruning - throw out strings that are too big for any of our queries
                    cur[k] = ncur[k]
        ret = []
        for x, y in queries:
            ret.append(ans[x ^ y] if (x^y) in ans else [-1, -1])
        return ret