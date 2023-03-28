class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        ret = -1
        def dfs(idx):
            nonlocal ret
            if idx == len(nums):
                ret += 1
                return
            v = nums[idx]
            if d[v] == 0:
                d[v-k] += 1
                d[v+k] += 1
                dfs(idx+1)
                d[v-k] -= 1
                d[v+k] -= 1
            dfs(idx+1)
        dfs(0)
        return ret