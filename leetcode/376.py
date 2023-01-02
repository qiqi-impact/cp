class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        def wig(pos):
            cur = nums[0]
            ln = 1
            for i in range(1, len(nums)):
                if nums[i] == cur:
                    continue
                if (nums[i] > cur and pos) or (nums[i] < cur and not pos):
                    ln += 1
                    pos = not pos
                cur = nums[i]
            return ln
        return max(wig(False), wig(True))