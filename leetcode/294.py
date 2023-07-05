class Solution:
    def canWin(self, currentState: str) -> bool:
        @cache
        def win(state):
            for i in range(len(state)-1):
                if state[i:i+2] == '++':
                    if not win(state[:i] + '--' + state[i+2:]):
                        return True
            return False
        return win(currentState)