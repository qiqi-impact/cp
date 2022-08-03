class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        ret = 0
        for i in range(len(jobs)):
            ret = max(ret, (jobs[i] + workers[i] - 1)//workers[i])
        return ret