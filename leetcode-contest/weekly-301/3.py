class Solution:
    def canChange(self, start: str, target: str) -> bool:
        a = []
        b = []
        for i, c in enumerate(start):
            if c != '_':
                a.append((i, c))
        for i, c in enumerate(target):
            if c != '_':
                b.append((i, c))
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i][1] != b[i][1]:
                return False
            if a[i][1] == 'L' and a[i][0] < b[i][0]:
                return False
            if a[i][1] == 'R' and a[i][0] > b[i][0]:
                return False
        # print(a, b)
        return True