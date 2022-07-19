class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(idx, amt):
            if idx == len(coins):
                return int(amt == 0)
            ret = 0
            for i in range(0, 1 + (amt // coins[idx])):
                ret += dfs(idx+1, amt - i * coins[idx])
            return ret
        return dfs(0, amount)