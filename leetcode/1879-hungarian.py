class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        g = []
        for i in range(len(nums1)):
            l = []
            for j in range(len(nums2)):
                l.append(nums1[i] ^ nums2[j])
            g.append(l)
        N = len(g) + 1
        M = len(g[0]) + 1
        U = [0] * N
        V = [0] * M
        P = [0] * M
        ans = [0] * (N-1)
        for i in range(1, N):
            P[0] = i
            j0 = 0;
            dist = [float('inf')] * M
            pre = [-1] * M
            done = [False] * (M+1)
            while 1:
                done[j0] = True
                i0 = P[j0]
                delta = float('inf')
                for j in range(1, M):
                    if not done[j]:
                        # print(i0-1, j-1, i0, j)
                        cur = g[i0 - 1][j - 1] - U[i0] - V[j]
                        if cur < dist[j]:
                            dist[j] = cur
                            pre[j] = j0
                        if dist[j] < delta:
                            delta = dist[j]
                            j1 = j
                for j in range(0, M):
                    if done[j]:
                        U[P[j]] += delta
                        V[j] -= delta
                    else:
                        dist[j] -= delta
                j0 = j1
                if not P[j0]:
                    break
            while j0:
                j1 = pre[j0]
                P[j0] = P[j1]
                j0 = j1
        for j in range(1, M):
            if P[j]:
                ans[P[j] - 1] = j - 1
        return -V[0]