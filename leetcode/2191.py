class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return [nums[i] for _, i in sorted([(int(''.join([str(x) for x in [mapping[int(c)] for c in str(nums[i])]])), i) for i in range(len(nums))])]