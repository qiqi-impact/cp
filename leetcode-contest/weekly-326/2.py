class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            for y in range(2, math.ceil(math.sqrt(x))+1):
                while not x%y:
                    x //= y
                    s.add(y)
                if y > x:
                    break
            if x != 1:
                s.add(x)
        return len(s)