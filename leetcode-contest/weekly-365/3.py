class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        sm = sum(nums)
        d = {0: -1}
        cur = 0
        pf = [0]
        
        nn = nums + nums
        ret = inf
        for i, x in enumerate(nn):
            cur += x
            pf.append(cur)
            t = (cur-target)%sm
            if t in d:
                idx = d[t]
                cat = cur - pf[idx+1]
                if target >= cat:
                    ret = min(ret, i - idx + (target - cat)//sm*len(nums))
            d[cur%sm] = i
        return ret if ret != inf else -1