class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        ret = [[0 for _ in range(C)] for _ in range(R)]
        for i in range(R-1, -1, -1):
            stack = []
            for j in range(C-1, -1, -1):
                while stack and heights[i][stack[-1]] < heights[i][j]:
                    stack.pop()
                    ret[i][j] += 1
                if stack:
                    ret[i][j] += 1
                if not stack or heights[i][stack[-1]] != heights[i][j]:
                    stack.append(j)
        for j in range(C-1, -1, -1):
            stack = []
            for i in range(R-1, -1, -1):
                while stack and heights[stack[-1]][j] < heights[i][j]:
                    stack.pop()
                    ret[i][j] += 1
                if stack:
                    ret[i][j] += 1
                if not stack or heights[stack[-1]][j] != heights[i][j]:
                    stack.append(i)
        return ret