class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ret = []
        q = 0
        for n in nums:
            ret.append(n)
            if len(ret) % 2 == 0 and ret[-1] == ret[-2]:
                ret.pop()
                q += 1
        return q + int(len(ret) % 2 == 1)
