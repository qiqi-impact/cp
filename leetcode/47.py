class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        s = set()
        used = set()
        path = []

        def dfs(idx):
            if idx == len(nums):
                s.add(tuple(path))
                return
            for i in range(len(nums)):
                if i not in used:
                    used.add(i)
                    path.append(nums[i])
                    dfs(idx+1)
                    path.pop()
                    used.discard(i)
        
        dfs(0)
        return list(s)