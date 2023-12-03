class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        sf = 0
        coins.sort()
        pt = 0
        ret = 0
        for i in range(1, target+1):
            while pt < len(coins) and coins[pt] <= max(sf, i):
                sf += coins[pt]
                pt += 1
            if i > sf:
                ret += 1
                sf += i
                # print(i)
        return ret