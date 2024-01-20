from functools import cache


SIGNATURE = [int, int, int, str]


from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums, k, dist):
        mn = 0
        for i in range(k):
            mn += nums[i]
            
        l, r = SortedList(), SortedList()
        
        hs = 0
        pt = 2
        
        for i in range(1, len(nums)):
            p = (nums[i], i)
            if l.count(p):
                l.discard(p)
                hs -= nums[i]
            if r.count(p):
                r.discard(p)
            while pt <= i+dist and pt < len(nums):
                np = (nums[pt], pt)
                r.add(np)
                pt += 1
            while r and len(l) < k-2:
                q = r.pop(0)
                l.add(q)
                hs += q[0]
            if len(l) == k-2:
                mn = min(mn, hs + nums[0] + nums[i])
            print(mn, len(l), l, r)
        return mn




print(Solution().minimumCost([6,40,41,11,50,15,47,48,50,12,16,30,38,45,13,34,26,25,32,28], 9, 13))


# with open("test_contest_in") as f:
#     tc = []
#     for i, l in enumerate(f.read().splitlines()):
#         if l[0] == '"' and l[-1] == '"':
#             l = l[1:-1]
#         l = SIGNATURE[i%len(SIGNATURE)](l)
#         tc.append(l)
#         if len(tc) == len(SIGNATURE):
#             print(Solution().F(*tc))
#             tc = []