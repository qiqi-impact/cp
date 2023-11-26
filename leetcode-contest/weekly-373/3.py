class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        t = sorted(range(n), key=lambda x:nums[x])
        
        l = [-1] * n
        q = []
        
        for i in range(n):
            if i == 0 or nums[t[i]] - nums[t[i-1]] > limit:
                q.append([])
            q[-1].append(nums[t[i]])
            l[t[i]] = len(q)-1
            
        for x in q:
            x.sort()
            
        ret = [None] * n
        for i in range(n-1, -1, -1):
            x = q[l[i]]
            ret[i] = x.pop()
        return ret