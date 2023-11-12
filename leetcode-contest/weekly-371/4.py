class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        root = {'t': 0}
        
        MX = 21
        def ins(v):
            cur = root
            cur['t'] += 1
            for i in range(MX, -1, -1):
                if v & (1 << i):
                    q = 1
                else:
                    q = 0
                if q not in cur:
                    cur[q] = {'t': 0}
                cur[q]['t'] += 1
                cur = cur[q]
        
        def kill(v):
            cur = root
            cur['t'] -= 1
            for i in range(MX, -1, -1):
                if v & (1 << i):
                    q = 1
                else:
                    q = 0
                cur[q]['t'] -= 1
                cur = cur[q]
                
        def find_max(v):
            cur = root
            ans = 0
            for i in range(MX, -1, -1):
                if v & (1 << i):
                    q = 0
                else:
                    q = 1
                if q in cur and cur[q]['t'] >= 1:
                    cur = cur[q]
                    ans ^= 1 << i
                else:
                    cur = cur[1-q]
            return ans
        
        j = 0
        ret = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] <= 2 * nums[i]:
                ins(nums[j])
                j += 1
            ret = max(ret, find_max(nums[i]))
            kill(nums[i])
        return ret
                
            
                