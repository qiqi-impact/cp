class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = defaultdict(int)
        bf = [0] * n
        
        ct = defaultdict(int)
        
        for i in range(1, k+1):
            if k%i==0:
                for j in range(n):
                    if nums[j]%i==0:
                        ct[i] += 1
                        bf[j] = i
        
        ret = 0
        for i in range(n):
            ret += ct[k//bf[i]]
            if nums[i] % (k//bf[i]) == 0:
                ret -= 1
        return ret//2