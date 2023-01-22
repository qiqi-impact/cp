class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mx = max(nums)
        ct = [0] * (mx+1)
        for x in nums:
            ct[x] += 1
        left, right = [0] * (mx+1), [0] * (mx+1)
        rp = mx
        tot = len(nums)//2
        for i in range(mx, 0, -1):
            if tot == 0:
                break
            if ct[i]:
                amt = min(tot, ct[i])
                right[i] += amt
                tot -= amt
            
        for i in range(mx+1):
            left[i] = ct[i] - right[i]
            if left[i]:
                lp = i
                
        for i in range(len(nums)):
            if i%2 == 0:
                nums[i] = lp
                left[lp] -= 1
                while lp > 0 and not left[lp]:
                    lp -= 1
            else:
                nums[i] = rp
                right[rp] -= 1
                while rp > 0 and not right[rp]:
                    rp -= 1