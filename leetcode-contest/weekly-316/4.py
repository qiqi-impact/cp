class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        a, b = [[], []], [[], []]
        for n in nums:
            a[n%2].append(n)
        for n in target:
            b[n%2].append(n)
        for i in range(2):
            a[i].sort()
            b[i].sort()
        ret = 0
        for i in range(len(a[0])):
            ret += abs(a[0][i] - b[0][i])//2
        for i in range(len(a[1])):
            ret += abs(a[1][i] - b[1][i])//2
        return ret//2