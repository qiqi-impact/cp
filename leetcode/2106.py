class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        fr = []
        seen_sp = False
        start_index = None
        for x, y in fruits:
            if x > startPos and not seen_sp:
                fr.append((startPos, 0))
                start_index = len(fr)-1
                seen_sp = True
            if x == startPos:
                start_index = len(fr)
                seen_sp = True
            fr.append((x, y))
        if not seen_sp:
            fr.append((startPos, 0))
            start_index = len(fr)-1

        def mxf(fx, si):
            r = si
            ps = [0]
            mx = 0
            for x, y in fx:
                ps.append(ps[-1] + y)
            for l in range(si+1):
                used = fx[si][0] - fx[l][0]
                if used > k: continue
                while r < len(fx)-1 and fx[r+1][0] <= fx[si][0] + k - 2 * used:
                    r += 1
                mx = max(mx, ps[r+1] - ps[l])
            return mx
        
        t = [(-x,y) for (x,y) in fr][::-1]
        return max(mxf(fr, start_index), mxf(t, len(fr)-1-start_index))