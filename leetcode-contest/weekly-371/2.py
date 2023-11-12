class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        def diff(a, b):
            A = int(a[:2]) * 60 + int(a[2:])
            B = int(b[:2]) * 60 + int(b[2:])
            return B - A
        d = {}
        s = set()
        access_times.sort(key=lambda x:x[1])
        for x, y in access_times:
            if x not in d:
                d[x] = []
            if len(d[x]) >= 2:
                if diff(d[x][0], y) < 60:
                    s.add(x)
                d[x] = d[x][1:]
            d[x].append(y)
        return list(s)
                