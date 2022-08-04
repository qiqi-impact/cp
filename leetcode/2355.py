class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        def triangle(n):
            return n*(n+1)//2
        
        def value(item):
            return triangle(item[0]) - triangle(item[0] - item[1])
        
        mx = 0
        stack = []
        sum_stack = 0
        for b in books:
            p = [b, 1]
            while stack and stack[-1][0] >= b - p[1]:
                p[1] += stack[-1][1]
                p[1] = min(p[0], p[1])
                sum_stack -= value(stack.pop())
            sum_stack += value(p)
            stack.append(p)
            mx = max(mx, sum_stack)
        return mx