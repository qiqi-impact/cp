class Solution:
    def minimumSum(self, num: int) -> int:
        l = sorted([int(x) for x in str(num)])
        ans = [0, 0]
        for i in range(len(l)):
            ans[i%2] = 10 * ans[i%2] + l[i]
        return sum(ans)