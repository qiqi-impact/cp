class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        R, C = len(grid), len(grid[0])
        D = list(itertools.pairwise([-1, 0, 1, 0, -1]))
        ans = {}
        sq = sorted(queries)
        vis = [[0 for _ in range(C)] for _ in range(R)]
        vis[0][0] = 1
        h = [(grid[0][0], 0, 0)]
        done = 0
        for q in sq:
            # print(q)
            # print()
            while h:
                if q > h[0][0]:
                    v, x, y = heapq.heappop(h)
                    # print(v, x, y)
                    done += 1
                    for dx, dy in D:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < R and 0 <= ny < C and not vis[nx][ny]:
                            heapq.heappush(h, (grid[nx][ny], nx, ny))
                            vis[nx][ny] = 1
                else:
                    break
            ans[q] = done
        return [ans[x] for x in queries]