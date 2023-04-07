class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        if minutes >= len(customers):
            return sum(customers)
        save = 0
        for i in range(minutes):
            if grumpy[i]:
                save += customers[i]
        mx = save
        for i in range(minutes, len(customers)):
            if grumpy[i]:
                save += customers[i]
            if grumpy[i-minutes]:
                save -= customers[i-minutes]
            mx = max(mx, save)
        ret = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                ret += customers[i]
        return ret + mx