class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        h = []
        n = len(nums)
        queries.sort()
        q = deque(queries)
        cur = 0
        end = defaultdict(int)
        take = 0
        for i in range(n):
            cur -= end[i]
            while q and q[0][0] <= i:
                heapq.heappush(h, -(1+q[0][1]))
                q.popleft()
            while cur < nums[i]:
                while 1:
                    if not h:
                        return -1
                    x = heapq.heappop(h)
                    x = -x
                    if x > i:
                        end[x] += 1
                        cur += 1
                        take += 1
                        break
                    else:
                        return -1
        return len(queries) - take