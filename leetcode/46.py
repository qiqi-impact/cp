class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ret = []
        path = []
        used = set()

        def dfs(idx):
            if idx == len(nums):
                ret.append(path[:])
                return
            for i in range(len(nums)):
                if i not in used:
                    used.add(i)
                    path.append(nums[i])
                    dfs(idx+1)
                    path.pop()
                    used.discard(i)
        dfs(0)
        return ret