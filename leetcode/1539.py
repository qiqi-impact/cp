class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = set(arr)
        for i in range(1, 3000):
            if i not in s:
                k -= 1
                if k == 0:
                    return i