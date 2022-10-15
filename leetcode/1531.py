import heapq

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        h = [(0, '-', 0, k, 0)]
        n = len(s)
        seen = set([('-', 0, k, 0)])
        while h:
            total, run_ch, run_len, k_left, idx = heapq.heappop(h)
            if idx == n:
                return total
            c = s[idx]
            if k_left >= 1:
                t = (run_ch, run_len, k_left - 1, idx + 1)
                if t not in seen:
                    heapq.heappush(h, (total, *t))
                    seen.add(t)
            if c == run_ch:
                new_total = total
                if run_len in [1, 9, 99]:
                    new_total += 1
                t = (run_ch, run_len + 1, k_left, idx + 1)
                if t not in seen:
                    heapq.heappush(h, (new_total, *t))
                    seen.add(t)
            else:
                t = (c, 1, k_left, idx + 1)
                if t not in seen:
                    heapq.heappush(h, (total + 1, *t))
                    seen.add(t)