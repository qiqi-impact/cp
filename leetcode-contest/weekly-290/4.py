class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        ch = {0: 0}
        for [x, y] in flowers:
            ch[x] = ch.get(x, 0) + 1
            ch[y+1] = ch.get(y+1, 0) - 1
        sk = sorted(list(ch.keys()))
        
        cum = {}
        cur = 0
        for k in sk:
            cur += ch[k]
            cum[k] = cur
        
        ps = [sk[bisect.bisect_right(sk, p)-1] for p in persons]
        return [cum[k] for k in ps]