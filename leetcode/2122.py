class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        print(nums)
        for gap in range(1, len(nums)//2+1):
            vis = [0] * len(nums)
            l = 0
            r = gap
            vis[l] = vis[r] = 1
            fail = False
            diff = nums[r] - nums[0]
            if diff <= 1 or diff % 2 == 1:
                continue
            ret = [(nums[r] + nums[0])//2]
            for i in range(len(nums)//2-1):
                while vis[l]:
                    l += 1
                while vis[r] or nums[r] - nums[l] < diff:
                    r += 1
                    if r == len(nums) or nums[r] - nums[l] > diff:
                        fail = True
                        break
                if fail:
                    break
                vis[l] = vis[r] = 1
                ret.append((nums[r] + nums[l])//2)
            if not fail:
                return ret