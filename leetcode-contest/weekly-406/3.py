class Solution:
    def minimumCost(self, m: int, n: int, h: List[int], v: List[int]) -> int:
        v.sort(reverse=True)
        h.sort(reverse=True)
        hp = vp = ret = 0
        while hp < len(h) or vp < len(v):
            if hp == len(h):
                ch = 2
            elif vp == len(v):
                ch = 1
            else:
                if h[hp] <= v[vp]:
                    ch = 2
                else:
                    ch = 1
            if ch == 1:
                ret += h[hp] * (vp + 1)
                hp += 1
            else:
                ret += v[vp] * (hp + 1)
                vp += 1
        return ret