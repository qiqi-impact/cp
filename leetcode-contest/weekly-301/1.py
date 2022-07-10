class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        if 2 * amount[-1] >= sum(amount):
            return amount[-1]
        return (sum(amount) + 1)//2