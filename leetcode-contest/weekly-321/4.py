class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = defaultdict(int)
        r = defaultdict(int)
        l[0] = r[0] = 1

        for i in range(len(nums)):
            if nums[i] == k:
                st = i
                break
        cum = 0
        for i in range(st-1, -1, -1):
            x = 1 if nums[i] > k else -1
            cum += x
            l[cum] += 1
        cum = 0
        for i in range(st+1, len(nums)):
            x = 1 if nums[i] > k else -1
            cum += x
            r[cum] += 1
        ret = 0
        for k in l:
            for sm in [0, 1]:
                rk = sm - k
                ret += l[k] * r[rk]
        return ret