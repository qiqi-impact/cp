class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ret = 0
        for i in range(k):
            x = happiness[i]
            ret += max(0, x - i)
        return ret