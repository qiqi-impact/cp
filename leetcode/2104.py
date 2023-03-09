class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        mn = []
        mx = []
        ret = 0
        mns = 0
        mxs = 0
        for i, n in enumerate(nums):
            lst = i
            while mn and n <= mn[-1][0]:
                x, y = mn.pop()
                mns += (n - x) * (lst - y)
                lst = y
            mn.append((n, lst))
            mns += n
            
            lst = i
            while mx and n >= mx[-1][0]:
                x, y = mx.pop()
                mxs += (n - x) * (lst - y)
                lst = y
            mx.append((n, lst))
            mxs += n
            
            ret += mxs - mns
        return ret