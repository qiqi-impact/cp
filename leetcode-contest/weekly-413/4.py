class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        xor = [[0 for _ in range(n)] for _ in range(n)]
        ans = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            xor[i][i] = ans[i][i] = nums[i]
        for df in range(1, n):
            for i in range(n-df):
                xor[i][i+df] = xor[i][i+df-1] ^ xor[i+1][i+df]
                ans[i][i+df] = max(xor[i][i+df], ans[i][i+df-1], ans[i+1][i+df])
        return [ans[x][y] for x, y in queries]
