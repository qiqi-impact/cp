class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ret = []
        for x, y in zip(l, r):
            if y - x < 2:
                ret.append(True)
            else:
                h = []
                s = defaultdict(int)
                for i in range(x, y+1):
                    v = nums[i]
                    s[v] += 1
                    heapq.heappush(h, v)
                    if len(h) > 2:
                        heapq.heappop(h)
                df = h[1] - h[0]
                st = h[1]
                ans = True
                for j in range(y - x + 1):
                    if s[st] == 0:
                        ans = False
                        break
                    else:
                        s[st] -= 1
                        st -= df
                ret.append(ans)
        return ret