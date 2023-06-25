class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        f = [int(str(x)[0]) for x in nums]
        l = [int(str(x)[-1]) for x in nums]
        ret = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if math.gcd(f[i], l[j]) == 1:
                    ret += 1
        return ret