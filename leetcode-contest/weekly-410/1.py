class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        r, c = 0, 0
        for x in commands:
            if x == 'LEFT':
                c -= 1
            elif x == 'RIGHT':
                c += 1
            elif x == 'DOWN':
                r += 1
            else:
                r -= 1
        return r * n + c