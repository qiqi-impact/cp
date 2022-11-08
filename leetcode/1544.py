class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1].lower() != c.lower() or stack[-1] == c:
                stack.append(c)
            else:
                stack.pop()
        return ''.join(stack)