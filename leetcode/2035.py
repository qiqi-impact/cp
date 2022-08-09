class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//2
        
        def dfs(arr, idx):
            if idx == len(arr):
                x = defaultdict(list)
                x[0] = [0]
                return x
            nd = dfs(arr, idx+1)
            for k in range(len(arr)-1, -1, -1):
                for e in nd[k]:
                    nd[k+1].append(2 * arr[idx] + e)
            return nd
        
        ll = dfs(nums[:n], 0)
        rr = dfs(nums[n:], 0)
        mn = float('inf')
        sl = sum(nums[:n])
        sr = sum(nums[n:])
        
        for i in range(0, n+1):
            l = sorted([x-sl for x in ll[i]])
            r = sorted([x-sr for x in rr[i]])
            lp = rp = 0
            while lp < len(l) and rp < len(r):
                mn = min(mn, abs(l[lp] - r[rp]))
                if l[lp] < r[rp]:
                    lp += 1
                else:
                    rp += 1
        return mn