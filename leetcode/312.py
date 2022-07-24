class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [x for x in nums if x != 0]
        prv = [-1] * len(nums)
        nxt = [-1] * len(nums)
        for i in range(len(nums)-1):
            nxt[i] = i+1
        for i in range(1, len(nums)):
            prv[i] = i-1
            
        ret = 0
        amt = len(nums)
        def remove(idx):
            nonlocal ret, amt
            p = prv[idx]
            n = nxt[idx]
            ret += nums[idx] * (1 if p == -1 else nums[p]) * (1 if n == -1 else nums[n])
            nxt[p] = n
            prv[n] = p
            nums[idx] = None
            amt -= 1
            # print(idx, ret)
            
        h = []

        
        for i in range(len(nums)):
            if nums[i] == 1:
                remove(i)
        
        left = None
        for i in range(len(nums)):
            if nums[i] is not None:
                left = i
                break
        if left is None: return ret
        right = None
        for i in range(len(nums)-1, -1, -1):
            if nums[i] is not None:
                right = i
                break
                
        for i in range(len(nums)):
            if nums[i] is not None and i != right and i != left:
                heapq.heappush(h, (nums[i], i))
        
        while 1:
            if amt == 0:
                return ret
            elif amt == 1:
                for i in range(len(nums)):
                    if nums[i] is not None:
                        return ret + nums[i]
            elif amt == 2:
                return ret + (min(nums[left], nums[right])+1)*max(nums[left], nums[right])
            else:
                _, idx = heapq.heappop(h)
                remove(idx)
        return ret
                