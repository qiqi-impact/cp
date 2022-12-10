class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)
        ret = []
        for i in range(len(pos)):
            ret.append(pos[i])
            ret.append(neg[i])
        return ret