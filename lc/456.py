class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ml = []
        for n in nums:
            if not ml or ml[-1] > n:
                ml.append(n)
            else:
                ml.append(ml[-1])
        stack = []
        for j in range(len(nums)-1, -1, -1):
            while stack and stack[-1] <= ml[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False