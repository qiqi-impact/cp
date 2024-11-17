class Solution:
    def countValidSelections(self, nn: List[int]) -> int:
        n = len(nn)
        def sim(x, dr):
            nums = nn[:]
            cur = x
            d = dr
            while 1:
                if not (0 <= cur <= n-1):
                    break
                if nums[cur] == 0:
                    cur += d
                elif nums[cur] > 0:
                    nums[cur] -= 1
                    d = -d
                    cur += d
            for x in nums:
                if x != 0:
                    return False
            return True
        ret = 0
        for i in range(n):
            if nn[i] == 0:
                for j in [-1, 1]:
                    if sim(i, j):
                        ret += 1
        return ret