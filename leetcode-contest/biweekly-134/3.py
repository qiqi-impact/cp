class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l = []
        for i in range(len(colors)):
            l.append(int(colors[i] != colors[(i+1)%len(colors)]))
        if sum(l) == len(l):
            return len(l)
        if sum(l) == 0:
            return 0
        for i in range(len(l)):
            if l[i] == 1 and l[(i-1)%len(l)] == 0:
                st = i
                break
        # print(l)
        ret = 0
        cur = 0
        for i in range(st, st + len(l)):
            if l[i%len(l)] == 1:
                cur += 1
                if cur >= k - 1:
                    ret += 1
            else:
                cur = 0
        return ret