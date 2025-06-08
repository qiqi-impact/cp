from sortedcontainers import SortedList

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        n = len(nums)

        sl = SortedList()
        q = deque()

        dp = [1]
        sdp = [0, 1]
        for i, x in enumerate(nums):
            q.append((x, i))
            sl.add((x, i))
            while sl and sl[-1][0] - sl[0][0] > k:
                a, b = q.popleft()
                sl.discard((a, b))
            
            first = q[0][1]
            v = (sdp[i + 1] - sdp[first]) % MOD
            dp.append(v)
            sdp.append((sdp[-1] + dp[-1]) % MOD)
            # print(i, q, dp, sdp)
        return dp[-1]
            