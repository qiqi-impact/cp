class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        la, lb = -inf, -inf
        diff = 0
        for i, x in enumerate(player1):
            m = 2 if (i - la <= 2) else 1
            diff += m * x
            if x == 10:
                la = i
        for i, x in enumerate(player2):
            m = 2 if (i - lb <= 2) else 1
            diff -= m * x
            if x == 10:
                lb = i
        if diff > 0:
            return 1
        elif diff < 0:
            return 2
        return 0