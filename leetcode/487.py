class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = []
        lst = None
        ct = 0
        for n in nums:
            if n != lst:
                if lst is not None:
                    l.append((lst, ct))
                ct = 1
                lst = n
            else:
                ct += 1
        l.append((lst, ct))
        ret = 1
        for i, (x, y) in enumerate(l):
            if x == 1:
                ret = max(ret, y)
            if x == 0:
                q = 1
                if i > 0:
                    q += l[i-1][1]
                    ret = max(ret,l[i-1][1]+1)
                if i < len(l)-1:
                    q += l[i+1][1]
                    ret = max(ret,l[i+1][1]+1)
                if y == 1:
                    ret = max(ret, q)
        return ret