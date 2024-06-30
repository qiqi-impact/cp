class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        mx = 0
        for l in [[red, blue], [blue, red]]:
            for i in range(1, 100000):
                idx = i%2
                if l[idx] < i:
                    break
                l[idx] -= i
                mx = max(mx, i)
        return mx