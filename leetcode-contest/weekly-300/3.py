class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        l = [0]
        for i in range(len(nums1)):
            l.append(abs(nums1[i] - nums2[i]))
        moves = k1 + k2
        if moves >= sum(l):
            return 0
        l.sort()
        lp = len(l)-1
        while 1:
            df = l[lp] - l[lp-1]
            amt = len(l) - lp
            if moves >= amt*df:
                moves -= amt*df
                lp -= 1
            else:
                x = moves%amt
                y = amt - x
                ret = 0
                for i in range(lp):
                    ret += l[i]**2
                left = l[lp]-moves//amt
                ret += y * (left**2) + x * ((left-1)**2)
                return ret