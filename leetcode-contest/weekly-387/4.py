from sortedcontainers import SortedList

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        c, d = [nums[0]], [nums[1]]
        a, b = SortedList(c), SortedList(d)
        for i in range(2, len(nums)):
            ia = len(a) - a.bisect_left(nums[i]+1)
            ib = len(b) - b.bisect_left(nums[i]+1)
            if ia > ib:
                wh = 1
            elif ia < ib:
                wh = 2
            else:
                if len(c) > len(d):
                    wh = 2
                else:
                    wh = 1
            if wh == 1:
                a.add(nums[i])
                c.append(nums[i])
            else:
                b.add(nums[i])
                d.append(nums[i])
        return c + d