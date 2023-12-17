class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ret = []
        n = len(nums)
        for i in range(n//3):
            ret.append([])
            for j in range(3):
                ret[-1].append(nums[i*3+j])
                if j ==2 and nums[i*3+j] - nums[i*3+j-2] > k:
                    return []
        return ret