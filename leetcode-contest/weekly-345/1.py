class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        vis = [0] * n
        vis[0] = 1
        cur = 0
        for i in range(1, 1000):
            cur += i*k
            cur %= n
            vis[cur] += 1
            if vis[cur] == 2:
                ret = []
                for i in range(n):
                    if not vis[i]:
                        ret.append(i+1)
                return ret