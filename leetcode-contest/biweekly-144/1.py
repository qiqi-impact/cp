class Solution:
    def canAliceWin(self, n: int) -> bool:
        cur = 10
        turn = 0
        while 1:
            if cur > n:
                return turn == 1
            n -= cur
            turn = 1 - turn
            cur -= 1