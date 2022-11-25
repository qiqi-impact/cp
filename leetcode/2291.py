class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        m = [[None for _ in range(budget+1)] for _ in range(len(present)+1)]
        
        m[-1] = [0] * (budget+1)
        
        for i in range(len(present)-1, -1, -1):
            for j in range(budget+1):
                m[i][j] = m[i+1][j]
                if j >= present[i]:
                    m[i][j] = max(m[i][j], future[i] - present[i] + m[i+1][j - present[i]])
        return m[0][budget]