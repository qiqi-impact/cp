class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        logs = [[-1,0]] + logs
        d = defaultdict(int)
        mx = -1
        mni = 0
        for i in range(1, len(logs)):
            e = logs[i][0]
            d[e] = max(d[e], logs[i][1] - logs[i-1][1])
            if d[e] > mx:
                mx = d[e]
                mni = e
            elif d[e] == mx:
                mni = min(e, mni)
        return mni