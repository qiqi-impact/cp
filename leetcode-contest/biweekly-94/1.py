class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        ret = 0
        for i in range(n):
            if forts[i] == -1:
                cur = 0
                for j in range(i-1, -1, -1):
                    if forts[j] == 0:
                        cur += 1
                    elif forts[j] == -1:
                        break
                    else:
                        ret = max(ret, cur)
                        break
                cur = 0
                for j in range(i+1, n):
                    if forts[j] == 0:
                        cur += 1
                    elif forts[j] == -1:
                        break
                    else:
                        ret = max(ret, cur)
                        break
        return ret